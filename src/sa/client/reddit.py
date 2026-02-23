from praw import Reddit  # type: ignore[import-untyped]


class RedditClient(Reddit):
    """A wrapper around the PRAW Reddit client that provides additional functionality for interacting with Reddit."""


def create_reddit_client(client_id: str, secret: str, user_agent: str) -> RedditClient:
    return RedditClient(
        client_id=client_id,
        client_secret=secret,
        user_agent=user_agent,
    )
