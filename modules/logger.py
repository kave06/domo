import logging

# Global variables
DB_HOST = '157.88.58.134'
DB_PORT = '5584'
DB_USER = 'kave'
DB_PASS = 'hola'
DB_NAME = 'cliente1'

'''
logging.basicConfig(filename='lm35_2.log',
                    level=logging.DEBUG,
                    filemode='w',
                    # format='%(asctime)s %(levelname)-8s %(message)s')
                    # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
                    #format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s %(pathname)s %(lineno)s')
'''


# create logger
def create_log() -> logging:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('controller.log', mode='w')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    logger.findCaller()
    # formatter = logging.Formatter('%(asctime)s %(funcName)s:%(lineno)s %(levelname)-8s '
    #                              '%(message)s')
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(funcName)-15s:%(lineno)-3s  '
                                  '%(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


# 'application' code
'''
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
'''
