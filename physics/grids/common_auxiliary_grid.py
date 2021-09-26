from physics.grids.any_common_grid import AnyCommonGrid
from physics.grids.any_auxiliary_grid import AnyAuxiliaryGrid
from physics.grids.common_grid import CommonGrid
from physics import Interval

from overrides import overrides

from functools import cached_property

__all__ = ['CommonAuxiliaryGrid']


class CommonAuxiliaryGrid(AnyCommonGrid, AnyAuxiliaryGrid):
    source: AnyCommonGrid

    def __init__(self, grid: AnyCommonGrid):
        self.source = grid

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return self.__value.points

    @overrides
    def point(self, i: int) -> float:
        return self.__value.point(i)

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.source.interval

    @property  # type: ignore
    @overrides
    def n(self) -> int:
        return self.__value.n

    @overrides
    def h(self, i: int) -> float:
        return self.__value.h(i)

    @overrides
    def point_with_half(self, i: int) -> float:
        return self.point(i+1)

    @cached_property
    def __value(self) -> CommonGrid:
        points = self.source.points
        n = len(self.source.points)
        return CommonGrid(
            [points[0]]
            + [(points[i] + points[i-1]) / 2 for i in range(1, n)]
            + [points[n-1]]
        )
