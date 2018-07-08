import os
import logging

logging_file = os.path.join(os.getenv("HOME"), 'test.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    filename=logging_file,
    filemode='w',
    handlers=[]
)

logging.debug('123')
