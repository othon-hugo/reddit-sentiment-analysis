from enum import Enum

from .csv import CSVPosts
from .xlsx import XLSXPosts


class StorageFormat(Enum):
    CSV = "csv"
    XLSX = "xlsx"


__all__ = [
    "CSVPosts",
    "XLSXPosts",
    "StorageFormat",
]
