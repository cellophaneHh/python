# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LogHandler.py
   Description :  日志操作模块
   Author :       JHao
   date：          2017/3/6
-------------------------------------------------
   Change Activity:
                   2017/3/6: log handler
                   2017/9/21: 屏幕输出/文件输出 可选(默认屏幕和文件均输出)
-------------------------------------------------
"""
__author__ = 'JHao'

import os

import logging

from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
# log文件夹路径为当前文件所在目录的
LOG_PATH = os.path.join(CURRENT_PATH, 'log')

# 日志输出格式: [INFO] [test.py:3] [2018-07-07 08:33:45,521]\
#    [asdf] [MainThread:139787199612736]
FORMAT = ('[%(levelname)s] [%(filename)s:%(lineno)d] [%(asctime)s] '
          '[%(message)s] [%(threadName)s:%(thread)d]')
FILE_ENCODING = "utf-8"


class LogHandler(logging.Logger):
    """
    LogHandler
    """

    def __init__(self, name, level=DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __setFileHandler__(self, level=None):
        """
        set file handler
        :param level:
        :return:
        """
        # 初始化日志文件夹
        self.init_log_path()
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1,
                                                backupCount=15, encoding=FILE_ENCODING)
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter(FORMAT)

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        set stream handler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(FORMAT)
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def resetName(self, name):
        """
        reset name
        :param name:
        :return:
        """
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()

    def init_log_path(self):
        """
        LOG_PATH不存在时新建
        :return: 日志文件路径
        """
        print('log path: {}'.format(LOG_PATH))
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)


if __name__ == '__main__':
    log = LogHandler('test')
    log.info('this is a test msg')
    log.info('__file__: {}'.format(__file__))
    log.info(os.path.abspath(__file__))
    log.info(CURRENT_PATH)
    # log.info(ROOT_PATH)
    log.info(LOG_PATH)
    log.info("接收参数: %s", {'1': 1, "2": 2})
