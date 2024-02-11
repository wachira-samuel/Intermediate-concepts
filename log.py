import logging
logger=logging.getLogger(__name__)
logger.info("hello  world")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s,%(name)s,%(levelname)s,%(message)s,datefmat=%d|%m|%Y')

#Create handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler('Logging.py')

#level format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter=logging.Formatter('%(name)s,%(levelname)s,%(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')