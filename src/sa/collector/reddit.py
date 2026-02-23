from typing import TYPE_CHECKING, Generator, Optional

from sa.analysis import UNKNOWN_AUTHOR_PLACEHOLDER, matches_language, pack_post, preprocess_text

if TYPE_CHECKING:
    from logging import Logger

    from praw import Reddit  # type: ignore[import-untyped]
    from praw.models import Submission  # type: ignore[import-untyped]

    from sa.analysis import CategorizedKeywords, Category, Language, PostRecord


class RedditScrapper:
    def __init__(self, reddit_client: "Reddit", subreddit_name: str, logger: Optional[Logger]):
        self._client = reddit_client
        self._subreddit_name = subreddit_name
        self._logger = logger

    def collect(self, ckw: "CategorizedKeywords", lang: "Language", total_per_category: int = 50000) -> Generator[PostRecord]:
        """
        Coleta posts de um subreddit baseando-se nas categorias e palavras-chave.
        Retorna lista de dicionários com texto, categoria e palavra-chave associada.
        """

        content_hashes: set[str] = set()

        for category, words in ckw.items():
            total_per_word = total_per_category // len(words)

            for keyword in words:
                subreddit = self._client.subreddit(self._subreddit_name)

                # Pesquisa por palavra-chave no título ou texto
                for post in subreddit.search(keyword, sort="new", limit=total_per_word):
                    clean_post = self._preprocess_post(post, category, keyword)

                    if not self._check_post_language(clean_post, lang):
                        continue

                    if clean_post["content_hash"] in content_hashes:
                        continue

                    content_hashes.add(clean_post["content_hash"])

                    yield clean_post

                if len(content_hashes) >= total_per_word:
                    break

    def _preprocess_post(self, post: "Submission", category: "Category", keyword: str) -> PostRecord:
        preprocess_title = preprocess_text(post.title) or ""
        preprocess_content = preprocess_text(post.selftext) or ""

        return pack_post(
            post_id=str(post.id),
            title=preprocess_title,
            content=preprocess_content,
            author=str(post.author) if post.author else UNKNOWN_AUTHOR_PLACEHOLDER,
            category=category,
            keyword=keyword,
            subreddit=self._subreddit_name,
            created_at=post.created_utc,
        )

    def _check_post_language(self, post: "PostRecord", lang: "Language") -> bool:
        return matches_language(post["content"], lang) or matches_language(post["title"], lang)

    def _log(self, message: str) -> None:
        if self._logger:
            self._logger.info(message)
