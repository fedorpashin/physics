from abc import ABC, abstractmethod


class Partition(ABC):
    @property
    @abstractmethod
    def num_parts(self) -> int:
        pass


class NumParts(int):
    source: Partition

    def __new__(cls, source: Partition) -> 'NumParts':
        return super().__new__(cls, cls.__value(source))

    def __init__(self, source: Partition):
        self.source = source

    @staticmethod
    def __value(source: Partition) -> int:
        return source.num_parts
