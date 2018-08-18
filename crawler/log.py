# coding: utf-8

"""
日志

废弃，改用log_handler.py
"""

import logging
import logging.handlers as handlers
import sys
import os

# 日志输出格式: [INFO] [test.py:3] [2018-07-07 08:33:45,521]\
#    [asdf] [MainThread:139787199612736]
FORMAT = ('[%(levelname)s] [%(filename)s:%(lineno)d] [%(asctime)s] '
          '[%(message)s] [%(threadName)s:%(thread)d]')
FILE_ENCODING = "utf-8"


def get_logger():
    """
    初始日志配置信息
    :return: logger
    """
    lgr = logging.getLogger("crawler_logger")
    lgr.setLevel(logging.INFO)

    formatter = logging.Formatter(FORMAT)

    # 控制台输出
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    lgr.addHandler(console_handler)

    # 按日期文件输出
    path = get_log_path()
    timed_rotating_file_handler = handlers.TimedRotatingFileHandler(
        filename=path,
        encoding=FILE_ENCODING,
        backupCount=10,
        when='midnight')
    timed_rotating_file_handler.setFormatter(formatter)
    lgr.addHandler(timed_rotating_file_handler)

    return lgr


def get_log_path():
    """
    获取日志路径
    :return: 日志文件路径
    """
    log_path = os.path.join(os.getcwd(), 'log')
    print('log path: {}'.format(log_path))
    if not os.path.exists(log_path):
        print('不存在，新建')
        os.mkdir(log_path)
    return os.path.join(log_path, 'crawler_log.log')


logger = get_logger()
