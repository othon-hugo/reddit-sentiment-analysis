import pandas as pd
from typing import TYPE_CHECKING, Iterable
from pathlib import Path

if TYPE_CHECKING:
    from sa.analysis import PostRecord


from typing import Iterable
from pathlib import Path
import pandas as pd


class ExcelPosts:
    def __init__(self, path: str | Path, sheet_name: str = "posts"):
        self._path = Path(path)
        self._sheet_name = sheet_name

    def save(self, posts: Iterable["PostRecord"]) -> None:
        posts_list = list(posts)

        if not posts_list:
            raise ValueError("Nenhum post para exportar.")

        df = pd.DataFrame(posts_list)

        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

        df.to_excel(self._path, index=False, sheet_name=self._sheet_name)
