import datetime

min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)

print(min6, ':', d)
print(datetime.timezone.utc, ':',
      d.astimezone(datetime.timezone.utc))
print(plus6, ":", d.astimezone(plus6))

d_system = d.astimezone()
print(d_system.tzinfo, "  :", d_system)

d = datetime.datetime.now()

# 这个函数可以根据时区打印时间
# 不传递时区参数为默认当前系统时区
print(d.astimezone())
print(d.astimezone(min6))

print(type(d.astimezone()))
print(d.strftime('%Y-%m-%d %H:%M:%S'))
