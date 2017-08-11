import logging

# Global variables
DB_HOST = '157.88.58.134'
DB_PORT = '5584'
DB_USER = 'kave'
DB_PASS = 'hola'
DB_NAME = 'cliente1'

logging.basicConfig(filename='lm35_2.log',
                    level=logging.DEBUG,
                    filemode='w',
                    # format='%(asctime)s %(levelname)-8s %(message)s')
                    # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')



# create logger
def create_log():
    return logging.getLogger(__name__)


# 'application' code
'''
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
'''
