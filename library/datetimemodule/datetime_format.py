'''
格式化日期
'''
import datetime

today = datetime.datetime.today()
print('ISO: ', today)
print('format(): {:%Y-%m-%d %H:%M:%S}'.format(today))
