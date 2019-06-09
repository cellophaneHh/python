import pymysql


def execute_sql(sql):
    try:
        print("开始连接..")
        db = pymysql.connect("127.0.0.1", "test", "123456", "test")
        cursor = db.cursor()
        print("开始执行...")
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        try:
            db.close()
        except Exception as e1:
            print(e1)


users = execute_sql("select * from user")
print(type(users))
print(users)
