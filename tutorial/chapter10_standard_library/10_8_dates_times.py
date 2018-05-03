"""
时间API
"""
from datetime import date

now = date.today()
print(now)
print(type(now))

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

yesterday = date(2018, 5, 2)
age = now - yesterday
print(age.days)

