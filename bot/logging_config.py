import logging
#setting up logger
def setup_logger():
 logger=logging.getLogger('trade_bot')
 logger.setLevel(logging.INFO)
 #creating file handler
 fh=logging.FileHandler('bot.log')
 fh.setLevel(logging.INFO)
 #creating console handler
 ch=logging.StreamHandler()
 ch.setLevel(logging.INFO)
 formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
 fh.setFormatter(formatter)
 ch.setFormatter(formatter)
 logger.addHandler(fh)
 logger.addHandler(ch)
 return logger
