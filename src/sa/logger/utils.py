from logging import INFO
from logging import Logger as _Logger
from logging import StreamHandler


class Logger(_Logger):
    pass


def create_logger(name: str) -> Logger:
    logger = Logger(name)
    logger.setLevel(INFO)

    handler = StreamHandler()
    logger.addHandler(handler)

    return logger
