from physics.grids.any_common_grid import AnyCommonGrid
from physics import Interval

from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['Grid']


@final
@dataclass
class CommonGrid(AnyCommonGrid):
    __points: list[float]

    def __init__(self, points: list[float]):
        self.__points = points

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return self.__points

    @overrides
    def point(self, i: int) -> float:
        return self.points[i]

    @cached_property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return Interval(self.points[0], self.points[-1])

    @property  # type: ignore
    @overrides
    def n(self) -> int:
        return len(self.points) - 1

    @overrides
    def h(self, i: int) -> float:
        return self.points[i] - self.points[i-1]

    @overrides
    def ħ(self, i: int) -> float:
        if i == 0:
            return self.h(1) / 2
        elif i == self.n:
            return self.h(self.n) / 2
        else:
            return (self.h(i) + self.h(i+1)) / 2
