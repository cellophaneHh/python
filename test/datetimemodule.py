import datetime

format = "%Y-%m-%d %H-%M-%S"

now = datetime.datetime.today()
print(now)
c = now.strftime(format)

now = datetime.datetime.strptime(c, format)
print(type(now))
print(now)
