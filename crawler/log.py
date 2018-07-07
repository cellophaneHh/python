# coding: utf-8

"""
日志
"""

import logging
import logging.handlers as handlers
import sys
import os

# 日志输出格式，[INFO] [Log4j.java:95] [2018.06.19 17:25:29] [日志本体] [main:id]
FORMAT = '[%(levelname)s] [%(filename)s:%(lineno)d] [%(asctime)s] [%(message)s] [%(threadName)s:%(thread)d]'
FILE_ENCODING = "utf-8"


def get_logger():
    """
    初始日志配置信息
    :return: logger
    """
    formatter = logging.Formatter(FORMAT)
    lgr = logging.getLogger("recoder")

    # 控制台输出
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    lgr.setLevel(logging.INFO)
    lgr.addHandler(console_handler)

    path = get_log_path()

    # 按日期文件输出
    timed_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=path, encoding=FILE_ENCODING,
                                                                    backupCount=10, when='midnight')
    timed_rotating_file_handler.setFormatter(formatter)
    lgr.addHandler(timed_rotating_file_handler)
    return lgr


def get_log_path():
    """
    获取日志路径
    :return: 日志文件路径
    """
    log_path = os.getcwd() + "/log"
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return log_path + "/crawler_log.log"


logger = get_logger()

