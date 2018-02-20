import logging


class Log(object):
    def __init__(self, log_path):
        logging.basicConfig(filename=log_path,level=logging.DEBUG)

    def writeToLog(self, message):
        logging.info(message)
