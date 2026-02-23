from praw import Reddit  # type: ignore[import-untyped]


def create_reddit_client(client_id: str, secret: str, user_agent: str) -> Reddit:
    return Reddit(
        client_id=client_id,
        client_secret=secret,
        user_agent=user_agent,
    )
