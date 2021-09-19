from physics import Interval

from abc import ABC, abstractmethod

__all__ = ['AnyGrid']


class AnyGrid(ABC):
    @property
    @abstractmethod
    def points(self) -> list[float]:
        pass

    @abstractmethod
    def point(self, i) -> float:
        pass

    @property
    @abstractmethod
    def interval(self) -> Interval:
        pass

    @property
    @abstractmethod
    def n(self) -> int:
        pass
