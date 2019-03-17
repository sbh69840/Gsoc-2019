import logging
logging.basicConfig(filename="my.log",filemode="w",level=logging.DEBUG,\
format='%(asctime)s - %(levelname)-10s - %(message)s')
logging.info("I did it")