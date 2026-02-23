from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class FileSaverABC(ABC, Generic[T]):
    @abstractmethod
    def save(self, values: Iterable[T]) -> None: ...


class FileConverterABC(ABC):
    @abstractmethod
    def convert(self, input_path: str, output_path: str) -> None:
        pass
