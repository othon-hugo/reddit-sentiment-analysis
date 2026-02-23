from hashlib import md5
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from pandas import Timestamp

    from sa.model.polarity import Polarity

UNKNOWN_AUTHOR_PLACEHOLDER = "[UNKNOWN-AUTHOR]"


class PostRecord(TypedDict):
    post_id: str
    title: str
    content: str
    content_hash: str
    author: str
    category: str
    keyword: str
    subreddit: str
    created_at: "Timestamp"


def pack_post(
    post_id: str,
    title: str,
    content: str,
    author: str,
    keyword: str,
    category: "Polarity",
    subreddit: str,
    created_at: "Timestamp",
) -> PostRecord:
    """Empacota um post coletado por categoria."""

    content_hash = md5(content.encode()).hexdigest()

    return {
        "post_id": post_id,
        "title": title,
        "content": content,
        "content_hash": content_hash,
        "author": author,
        "keyword": keyword,
        "category": category.value,
        "subreddit": subreddit,
        "created_at": created_at,
    }
