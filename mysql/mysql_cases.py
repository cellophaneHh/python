import pymysql

db = pymysql.connect('localhost', 'root', '1234qwer', 'test')

cursor = db.cursor()

cursor.execute('show tables')

data = cursor.fetchall()

print(data)

cursor.execute('select * from employee')

data = cursor.fetchmany(2)

print(data)

db.close()
