from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class FileABC(ABC, Generic[T]):
    @abstractmethod
    def save(self, values: Iterable[T]) -> None: ...
