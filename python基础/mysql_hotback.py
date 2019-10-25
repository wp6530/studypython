# coding: utf-8
import os
import sys
import subprocess
import json
import datetime
from time import sleep
import shutil
import argparse
import logging
import logging.handlers


def _wrap_with(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)

    return inner


red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')


def get_now_time():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')


logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

back_log = "/var/log/xtrabackup_mysql.log"

rf_handler = logging.handlers.TimedRotatingFileHandler(
    back_log, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(rf_handler)


class HotBackupMysql(object):
    def __init__(self, json_file=None):
        self.json_file = json_file

        # 配置文件读取部分
        self.cnf_file = ""
        self.mysql_bin_path = ""
        self.host = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.host_alias = ""

        self.work_path = ""
        self.db_list = ""
        self.store_day = ""
        self.iops = ""
        self.use_memeory = ""
        self.backup_base = ""
        self.backup_hour = ""

        # 自定义部分
        self.log_file = back_log
        self.backup_path = ""
        self.db_backup_file_name = ""
        self.socket = ""
        self.lock_file = ""

    def test_key_value(self, key1, key2, default_value=""):
        """
        如果检查到key未空，则把default-value赋值给key
        """
        key = setattr(self, key1).setattr()
        if not key:
            key = default_value
            return key

    def parse_json(self):
        """
        默认值设定在页面里做好了
        """
        try:
            with open(self.json_file) as f:
                json_file_content = f.readlines()
        except Exception as e:
            mess = "打开配置文件失败, %s" % e
            logger.error(message=mess)
            return False
        config_dict = json.loads("".join(json_file_content), encoding="utf-8")
        self.cnf_file = config_dict["config"]["cnf_file"]
        self.mysql_bin_path = config_dict["config"]["mysql_bin_path"]
        self.host = config_dict["config"]["host"]
        self.port = config_dict["config"]["port"]
        self.user = config_dict["config"]["user"]
        self.password = config_dict["config"]["password"]
        self.host_alias = config_dict["config"]["host_alias"]

        self.work_path = config_dict["backup_conf"]["work_path"]
        self.db_list = config_dict["backup_conf"]["db_list"]
        self.store_day = config_dict["backup_conf"]["store_day"]
        self.iops = config_dict["backup_conf"]["iops"]
        self.use_memeory = config_dict["backup_conf"]["use_memeory"]
        self.backup_base = config_dict["backup_conf"]["backup_base"]
        self.backup_path = "%s/database_%s" % (self.backup_base, self.port)
        self.check_backupdir()
        self.backup_hour = config_dict["backup_conf"]["backup_hour"]
        self.backup_type = config_dict["backup_conf"]["backup_type"]
        self.lock_file = "/var/lock/subsys/xtrabackup_%s" % self.port
        with open(self.cnf_file, "r") as f:
            content = f.readlines()
        for line in content:
            if line.startswith('socket'):
                self.socket = line.split("=")[1][:-1]
                break
        return self.backup_type

    def del_bak(self):
        """
        删除指定时间之前的日志
        """
        if int(self.store_day) < 3:
            logger.warning("根据设定参数%d, 删除后留存的数据库备份较少, 请手动删除" % (int(self.store_day)))
        cmd = """for dbfile in `find "{}/" -name "{}*.tar.gz" -type f -mtime +{}`;do\
             rm -f $dbfile;done""".format(self.backup_path, self.host_alias, self.store_day)
        status, output = subprocess.getstatusoutput(cmd)
        logger.info("[cmd: %s] %s" % (cmd, output))

    def check_xtrabackup(self):
        """
        检查安装工具是否安装
        """
        cmd = "rpm -q percona-xtrabackup-24"
        status, output = subprocess.getstatusoutput(cmd)
        if status:
            message = "need to install percona-xtrabackup-*.rpm, cmd output: [%s]" % output
            print(red(message))
            logger.error(message)
            return False
        return True

    def check_backupdir(self):
        """
        检查目录是否存在
        """
        if not os.path.isdir(self.backup_path):
            try:
                os.makedirs(self.backup_path)
                cmd = "chown -R nobody.nobody %s" % self.backup_path
                status, output = subprocess.getstatusoutput(cmd)
                message = "[cmd: %s] %s" % (cmd, output)
                logger.info(message)
            except Exception as e:
                message = "[cmd: %s] %s" % (cmd, output)
                logger.error(message)
                return False
        return True

    def all_backup(self):
        logger.info("Begin to backup all dbs")
        now_time = get_now_time()
        self.db_backup_file_name = "{}_{}_{}.tar.gz".format(self.host_alias, now_time, self.port)
        _dbbackup_file = "%s/%s" % (self.backup_path, self.db_backup_file_name)
        back_cmd = """xtrabackup --defaults-file={} --backup --use-memory={} --throttle={} --host={} \
                    --port={} --user={} --password={} --stream=tar --target-dir={} \
                    --no-lock 2>>{} | gzip - > {}
        """.format(self.cnf_file, self.use_memeory, self.iops, self.host, self.port,
                   self.user, self.password, self.backup_path, self.log_file, _dbbackup_file)
        logger.info(back_cmd)
        status1, output = subprocess.getstatusoutput(back_cmd)
        if status1:
            logger.error(output)
        else:
            logger.info(output)
        sleep(3)
        status2, output = subprocess.getstatusoutput("tail -50 \"%s\" | grep -ic \"\berror\b\"" % self.log_file)
        if status2:
            logger.error(output)
        else:
            logger.info(output)
        if not status1 and status2:
            get_xtrack_checkpoints_cmd = "cd %s;tar -zxf %s xtrabackup_checkpoints" % (self.backup_path, _dbbackup_file)
            logger.info(get_xtrack_checkpoints_cmd)
            subprocess.getstatusoutput(get_xtrack_checkpoints_cmd)
            self.del_bak()
            message = "Complete Hot Backup"
            logger.info(message)
            return True
        else:
            message = "[ERROR] error: xtrabackup failure, END!!"
            logger.info(message)
            return False, message

    def incr_backup(self):
        logger.info("Begin to TYPE INCR backup dbs")
        check_point_file = self.backup_path + "/xtrabackup_checkpoints"
        if not os.path.exists(check_point_file):
            logger.error("xtrabackup_checkpoints does not exist")
            self.all_backup()
            sleep(3)
        cmd = "awk '/to_lsn/ {print $3}' %s 2>/dev/null" % self.backup_path
        # logger.info(cmd)
        status, check_point = subprocess.getstatusoutput(cmd)
        logger.info("[cmd: %s] check_point is: %s" % (cmd, check_point))
        now_time = get_now_time()
        db_backup_file_name = "%s_%s_%s-increase" % (self.host_alias, now_time, self.port)
        db_backup_file = self.backup_path + "/" + db_backup_file_name
        backup_cmd = """ xtrabackup --backup --throttle={} --target-dir={} --incremental-lsn={} >>{}
        """.format(self.iops, db_backup_file, check_point, self.log_file)
        logger.info("[cmd: %s]" % (backup_cmd))
        status, output = subprocess.getstatusoutput(backup_cmd)
        if not status:
            tar_cmd = """cd {}; tar -zcf {}.tar.gz {}
            """.format(self.backup_path, db_backup_file_name, db_backup_file_name, )
            logger.info("[cmd: %s]" % (tar_cmd))
            stat1, out1 = subprocess.getstatusoutput(tar_cmd)
            sleep(3)
            incr_checkpoint_file = db_backup_file_name + "/xtrabackup_checkpoints"
            cmd = "cd %s;\cp %s %s" % (self.backup_path, incr_checkpoint_file, self.backup_path)
            stat2, out2 = subprocess.getstatusoutput(cmd)
            if stat2:
                print(red("拷贝文件失败，", out2))
                return False
            print("stat cp xtra file is ", stat2, out2)
            if db_backup_file_name not in ["", "/", ".", "/*", "/."]:
                stat3, out3 = subprocess.getstatusoutput("cd %s;rm -rf %s " % (self.backup_path, db_backup_file_name))
                print(stat3, out3)
            return True
        else:
            print(yellow("Incremental Hot Backup"))
            print(output)
            return False

    def backup_special_db(self):
        """
        备份指定库, 这一步需要先dump指定库的所有表
        """
        if not self.db_list:
            print(yellow("请指定数据库"))
            logger.warning("请指定数据库")
            return False
        try:
            file_name_string = "%s_%s_%s_DBLISTS" % (self.host_alias, get_now_time(), self.port)
            _BACKUP_TMP_DIR = "%s/%s" % (self.backup_base, get_now_time())
            if not os.path.isdir(_BACKUP_TMP_DIR):
                try:
                    cmd = "mkdir -p %s" % _BACKUP_TMP_DIR
                    status, output = subprocess.getstatusoutput(cmd)
                    logger.info(output)
                except Exception as e:
                    print("mkdir fail: ", e)
                    pass
            create_table_sql_file = _BACKUP_TMP_DIR + "/" + "db.sql"
            if len(self.db_list.split()) > 1:
                cmd = """mysqldump --add-drop-database -y -d -u{} -p{} --databases {} | sed 's/AUTO_INCREMENT=[0-9]*\s*//g' \
                    | sed '/^USE/d'| sed '/^CREATE DATABASE/d'> {}""".format(
                    self.user, self.password, self.db_list, create_table_sql_file)
            else:
                cmd = """mysqldump -y -d -u{} -p{} --databases {} | sed 's/AUTO_INCREMENT=[0-9]*\s*//g' > {}""".format(
                    self.user, self.password, self.db_list, create_table_sql_file)
            logger.info("[cmd: %s]" % cmd)
            status, output = subprocess.getstatusoutput(cmd)
            if status:
                mess = "%s" % output
                logger.error(mess)
                return False
        except Exception as e:
            # print(e)
            logger.error("[cmd: %s] %s" % (cmd, e))
            return False

        try:
            cmd = """ innobackupex --databases="{}" --user={} --password={} -S {} {} """.format(
                self.db_list, self.user, self.password, self.socket, _BACKUP_TMP_DIR)
            status, output = subprocess.getstatusoutput(cmd)
            if status:
                mes = "[cmd: %s] %s" % (cmd, output)
                print(mes)
                logger.error(cmd)
                return False
            cmd = "ls -d %s/* | grep -v db.sql" % _BACKUP_TMP_DIR
            stat_tmp, output_tmp = subprocess.getstatusoutput(cmd)
            if stat_tmp:
                print("ERROR=> ls -d", output_tmp)
                logger.error("[cmd: %s] %s" % (cmd, output_tmp))
                return False
            cmd = "innobackupex --apply-log --export %s" % output_tmp
            stat1, output1 = subprocess.getstatusoutput(cmd)
            if stat1:
                logger.error("[cmd: %s] %s" % (cmd, output1))
                return False
            cmd = "cd {} && tar -zcf {}/{}.tar.gz ./ db.sql".format(
                _BACKUP_TMP_DIR, self.backup_path, file_name_string)
            stat2, output2 = subprocess.getstatusoutput(cmd)
            if stat2:
                logger.error("[cmd: %s] %s" % (cmd, output2))
                return False
            else:
                logger.info("[cmd: %s] %s" % (cmd, output2))
            if _BACKUP_TMP_DIR and _BACKUP_TMP_DIR not in ["/", ".", "/*", "/."]:
                cmd = "rm -rf %s" % _BACKUP_TMP_DIR
                stat3, output3 = subprocess.getstatusoutput(cmd)
                if stat3:
                    print(red("ERROR: %s, DETAIL: %s" % (cmd, output3)))
                    logger.error("[cmd: %s] %s" % (cmd, output3))
            print(green("OK"))
            logger.info("[OK] success")
            return True
        except Exception as e:
            print(red(e))
            logger.error("[FAIL] %s" % e)
            return False, "fail"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf_file", "-f", required=True, type=str,
                        help="json file must specify and be absolute path")
    args = parser.parse_args()

    if not os.path.exists(args.conf_file):
        print(red("ERROR: must specify conf_file, pls check it"))
        sys.exit(1)
    conf_file = args.conf_file

    a = HotBackupMysql(json_file=conf_file)
    a.check_xtrabackup()
    backup_type = a.parse_json()
    a.del_bak()
    if backup_type == "zd_db":
        a.backup_special_db()
    if backup_type == "incr":
        a.incr_backup()
    if backup_type in ["", "all"]:
        a.all_backup()
