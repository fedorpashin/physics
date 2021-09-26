from physics.grids.any_uniform_grid import AnyUniformGrid
from physics import Interval
from physics.length import Length

from dataclasses import dataclass
from multimethod import multimethod
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['UniformGrid']


@final
@dataclass
class UniformGrid(AnyUniformGrid):
    __interval: Interval
    __num_parts: int

    def __init__(self, interval: Interval, num_parts: int):
        self.__interval = interval
        self.__num_parts = num_parts

    @cached_property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return [self.point(i) for i in range(self.num_parts + 1)]

    @overrides
    def point(self, i: int) -> float:
        return self.interval.l + i * self.__h

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.__interval

    @property  # type: ignore
    @overrides
    def num_parts(self) -> int:
        return self.__num_parts

    @multimethod
    @overrides
    def h(self, i: int) -> float:
        return self.__h

    @h.register  # type: ignore
    def h(self) -> float:
        return self.__h

    @cached_property
    def __h(self) -> float:
        return Length(self.interval) / self.num_parts
