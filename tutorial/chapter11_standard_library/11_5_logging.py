"""
日志记录模块
logging
默认warning
"""
import logging

logging.debug("Debugging information")
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


