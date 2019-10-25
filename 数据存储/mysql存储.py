import pymysql

# 连接数据库
db = pymysql.connect(
    host='192.168.190.131',
    user='liaozesong',
    db='my_sql',
    password='Lzslov123!',
    port=3306,
)

# 通过数据库连接下的cursor方法创建游标
cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()

# 查看数据库版本
# print("Database version:", data)

# 创建数据表
# cursor.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

# 插入数据
# 单条数据插入
# sqli = "insert into student values(%s,%s,%s,%s)"
# cursor.execute(sqli, ('3', 'Huhu', '2 year 1 class', '7'))

# 多条数据插入

# cursor.executemany(sqli,[
#     ('3', 'Tom', '1 year 1 class', '6'),
#     ('3', 'Jack', '2 year 1 class', '7'),
#     ('3', 'Yaheng', '2 year 2 class', '7'),
# ])

# 插入数据库，必须要commit，否则数据不会写入
# db.commit()


# 查询数据
lines = cursor.execute("select * from employees where emp_no=10001")
info = cursor.fetchmany(lines)
for i in info:
    print(i)
print(cursor.fetchone())


sql_drop = "DROP TABLE IF EXISTS  student"
cursor.execute(sql_drop)

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()
