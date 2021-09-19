from physics.grids.any_grid import AnyGrid
from physics.grids.grid import Grid
from physics import Interval

from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property


@final
@dataclass
class UniformGrid(AnyGrid):
    __interval: Interval
    __n: int

    def __init__(self, interval: Interval, n: int):
        self.__interval = interval
        self.__n = n

    @cached_property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return [self.point(i) for i in range(self.n + 1)]

    @overrides
    def point(self, i: int) -> float:
        return self.interval.l + i * self.h

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.__interval

    @property  # type: ignore
    @overrides
    def n(self) -> int:
        return self.__n

    @cached_property
    def h(self) -> float:
        return len(self.interval) / self.n
