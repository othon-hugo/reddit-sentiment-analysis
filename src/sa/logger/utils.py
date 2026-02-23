from logging import getLogger, Logger, INFO, StreamHandler


def get_logger(name: str) -> Logger:
    return getLogger(name)


def create_logger(name: str) -> Logger:
    logger = Logger(name)
    logger.setLevel(INFO)

    handler = StreamHandler()
    logger.addHandler(handler)

    return logger
