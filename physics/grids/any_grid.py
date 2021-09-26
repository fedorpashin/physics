from physics.partition import Partition
from physics import Interval

from abc import ABC, abstractmethod

__all__ = ['AnyGrid']


class AnyGrid(Partition, ABC):
    @property
    @abstractmethod
    def points(self) -> list[float]:
        pass

    @abstractmethod
    def point(self, i: int) -> float:
        pass

    @property
    @abstractmethod
    def interval(self) -> Interval:
        pass

    @abstractmethod
    def h(self, i: int) -> float:
        pass
