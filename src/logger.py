import logging
import os

class Logger:

    def __init__(self):
        if not os.path.exists('location.txt'):
            with open('location.txt', 'w'): pass
        logging.basicConfig(filename=r"location.txt", level=logging.INFO)

    def debug_log(self, message):
        logging.debug(message)
        print(message)

    def info_log(self, message):
        logging.info(message)
        print(message)

    def warning_log(self, message):
        logging.warning(message)
        print(message)

