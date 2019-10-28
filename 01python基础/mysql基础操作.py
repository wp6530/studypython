import pymysql

# 连接数据库
db = pymysql.connect(
    host='192.168.190.131',
    user='liaozesong',
    password='Lzslov123!',
    port=3306,
)
cursor = db.cursor()

# 查看数据库
sql_show_database = "SHOW DATABASES"
cursor.execute(sql_show_database)
# for x in cursor:
#     print(x)

# 查看数据表
# db = pymysql.connect(
#     host='192.168.190.131',
#     user='liaozesong',
#     password='Lzslov123!',
#     db='my_sql',
#     port=3306,
# )
# cursor = db.cursor()
# sql_show_tables = "SHOW TABLES"
# cursor.execute(sql_show_tables)
# for x in cursor:
#     print(x)

# 创建数据库
# sql_create_database = "CREATE DATABASE lab_sql"
# cursor.execute(sql_create_database)

# 创建数据表
# sql_create_table = "CREATE TABLE lab_sql.sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))"
# cursor.execute(sql_create_table)

# 插入数据
#
# sql_insert = "INSERT INTO lab_sql.sites (name, url) VALUES (%s, %s)"
# sql_val = ("RUNOOB", "https://www.runoob.com")
# sql_vals = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# cursor.execute(sql_insert, sql_val)
# cursor.executemany(sql_insert, sql_vals)
# db.commit()
# print(cursor.rowcount, "记录插入成功。")

# sql_select = "SELECT * FROM lab_sql.sites"
# sql_select = "SELECT name,url FROM lab_sql.sites"
# sql_select = "SELECT name,url FROM lab_sql.sites WHERE name='RUNOOB'"
sql_select = "SELECT name,url FROM lab_sql.sites WHERE url LIKE '%OO%'"


cursor.execute(sql_select)
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
db.close()






