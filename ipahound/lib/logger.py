import sys
import logging


class LoggerFormatter(logging.Formatter):

    def __init__(self):
        logging.Formatter.__init__(self, '%(bullet)s %(message)s', None)

    def format(self, record):
        if record.levelno is logging.INFO:
            record.bullet = '[+]'
        elif record.levelno is logging.WARNING:
            record.bullet = '[!]'
        elif record.levelno is logging.DEBUG:
            record.bullet = '[*]'
        elif record.levelno is logging.ERROR:
            record.bullet = '[-]'
        else:
            record.bullet = '[x]'

        return logging.Formatter.format(self, record)


def init_logging(debug=False):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(LoggerFormatter())

    logging.getLogger().addHandler(handler)

    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logging.basicConfig(level=logging.DEBUG)
