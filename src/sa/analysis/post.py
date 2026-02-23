from typing import TypedDict, Dict, List
from pandas import Timestamp
from enum import Enum
from hashlib import md5

UNKNOWN_AUTHOR_PLACEHOLDER = "[UNKNOWN-AUTHOR]"

CategorizedKeywords = Dict["Category", List[str]]


class Category(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class PostRecord(TypedDict):
    post_id: str
    title: str
    content: str
    content_hash: str
    author: str
    category: str
    keyword: str
    subreddit: str
    created_at: Timestamp


def pack_post(
    post_id: str,
    title: str,
    content: str,
    author: str,
    keyword: str,
    category: Category,
    subreddit: str,
    created_at: Timestamp,
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
