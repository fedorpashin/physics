from abc import ABC, abstractmethod


class HasLength(ABC):
    @property
    @abstractmethod
    def length(self):
        pass


class Length(float):
    source: HasLength

    def __new__(cls, source: HasLength) -> 'Length':
        return super().__new__(cls, cls.__value(source))

    def __init__(self, source: HasLength):
        self.source = source

    @staticmethod
    def __value(source: HasLength) -> float:
        return source.length
