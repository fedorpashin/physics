from physics.grids.any_grid import AnyGrid
from physics import Interval

from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property


@final
@dataclass
class Grid(AnyGrid):
    __points: list[float]

    def __init__(self, points: list[float]):
        self.__points = points

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return self.__points

    @overrides
    def point(self, i) -> float:
        return self.points[i]

    @cached_property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return Interval(self.points[0], self.points[-1])

    @property  # type: ignore
    @overrides
    def n(self) -> int:
        return len(self.points) - 1
