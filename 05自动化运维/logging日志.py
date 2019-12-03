# -*- coding=utf-8 -*-
import logging
import logging.config
# logging.basicConfig(filename='app.log', level=logging.INFO)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s:%(levelname)s:%(message)s',
#     filename="app.log"
# )
logging.config.fileConfig('logging.cnf')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
