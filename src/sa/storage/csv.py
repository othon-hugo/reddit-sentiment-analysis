import pandas as pd
from typing import TYPE_CHECKING, Iterable
from pathlib import Path

if TYPE_CHECKING:
    from sa.analysis import PostRecord


class CSVPosts:
    def __init__(self, path: str | Path):
        self._path = Path(path)

    def save(self, posts: Iterable["PostRecord"]) -> None:
        posts_list = list(posts)

        if not posts_list:
            raise ValueError("Nenhum post para exportar.")

        df: pd.DataFrame = pd.DataFrame(posts_list)

        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

        df.to_csv(self._path, index=False, encoding="utf-8")
