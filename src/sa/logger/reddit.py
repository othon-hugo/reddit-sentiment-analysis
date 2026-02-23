from logging import INFO, Formatter, Logger, StreamHandler


class RedditLogger(Logger):
    """
    Logger personalizado para o Reddit,
    configurado para exibir informações relevantes sobre a coleta de dados.
    """

    formatter = Formatter("%(asctime)s - r/%(name)s - %(levelname)s - %(message)s")


def create_reddit_logger(subreddit: str) -> RedditLogger:
    logger = RedditLogger(subreddit)
    logger.setLevel(INFO)

    handler = StreamHandler()
    handler.setFormatter(RedditLogger.formatter)

    logger.addHandler(handler)

    return logger
