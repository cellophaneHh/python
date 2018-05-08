"""
日期格式化
"""
import datetime
import time

def today_format(format):
    '''根据传入的格式格式化当前日期'''
    return datetime.date.today().strftime(format)

def datetime_format(format):
    """根据传入的格式格式化当前时间"""
    return datetime.datetime.now().strftime(format)

def timestamp():
    """获取当前的时间戳"""
    return time.mktime(datetime.datetime.now().timetuple())




