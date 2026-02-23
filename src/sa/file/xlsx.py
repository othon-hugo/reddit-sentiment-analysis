from pathlib import Path
from typing import TYPE_CHECKING, Iterable

import pandas as pd

from sa.common import FileReaderABC, FileSaverABC

if TYPE_CHECKING:
    from sa.model import PostRecord


class XLSXPostSaver(FileSaverABC["PostRecord"]):
    def __init__(self, path: str | Path, sheet_name: str = "posts"):
        self._path = Path(path)
        self._sheet_name = sheet_name

    def save(self, values: Iterable["PostRecord"]) -> None:
        posts_list = list(values)

        if not posts_list:
            raise ValueError("Nenhum post para exportar.")

        df = pd.DataFrame(posts_list)

        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

        df.to_excel(self._path, index=False, sheet_name=self._sheet_name)


class XLSXColumnReader(FileReaderABC[list[str]]):
    """Lê uma coluna específica de uma aba de um arquivo Excel, retornando uma lista de strings.

    Valores nulos são descartados automaticamente.

    Args:
        path: caminho do arquivo Excel.
        sheet_name: nome da aba a ser lida.
        column: nome da coluna a ser extraída.
    """

    def __init__(self, path: str | Path, sheet_name: str, column: str) -> None:
        self._path = Path(path)
        self._sheet_name = sheet_name
        self._column = column

    def read(self) -> list[str]:
        df: pd.DataFrame = pd.read_excel(self._path, sheet_name=self._sheet_name)

        if self._column not in df.columns:
            raise KeyError(f"Coluna '{self._column}' não encontrada na aba '{self._sheet_name}'.")

        df = df.dropna(subset=[self._column])

        return [str(v) for v in df[self._column]]
