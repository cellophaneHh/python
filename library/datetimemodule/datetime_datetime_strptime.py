"""
日期格式化
"""

import datetime

format = '%a %b %d %H:%M:%S %Y'

today = datetime.datetime.today()
print("ISO: ", today)

# 日期转字符串
s = today.strftime(format)
print(type(s))
print('striftime: ', s)

# 字符串转日期
d = datetime.datetime.strptime(s, format)
print(type(d))
print('strptime: ', d.strftime(format))
