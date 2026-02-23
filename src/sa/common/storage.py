from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Iterable

T = TypeVar("T")


class StorageABC(ABC, Generic[T]):
    @abstractmethod
    def save(self, values: Iterable[T]) -> None: ...
