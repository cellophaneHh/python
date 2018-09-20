import pymysql

db = pymysql.connect('localhost', 'root', '1234qwer', 'test')

cursor = db.cursor()

cursor.execute('show tables')

data = cursor.fetchall()

print(data)

db.close()
