import pymysql
db = pymysql.connect(host='106.14.107.230', user='ft', password='Sanguo1!', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print("Database version:", data)
db.close()