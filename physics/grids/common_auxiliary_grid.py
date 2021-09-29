from physics.grids.any_common_grid import AnyCommonGrid
from physics.grids.any_auxiliary_grid import AnyAuxiliaryGrid
from physics.grids.common_grid import CommonGrid
from physics import Interval

from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['CommonAuxiliaryGrid']


@final
@dataclass
class CommonAuxiliaryGrid(AnyCommonGrid, AnyAuxiliaryGrid):
    __source: AnyCommonGrid

    def __init__(self, grid: AnyCommonGrid):
        self.__source = grid

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return self.__value.points

    @overrides
    def point(self, i: int, with_half=False) -> float:
        return (
            self.__value.point(i+1) if with_half else
            self.__source.point(i)
        )

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.__source.interval

    @property  # type: ignore
    @overrides
    def num_parts(self) -> int:
        return self.__value.num_parts

    @overrides
    def h(self, i: int) -> float:
        return self.__value.h(i)

    @cached_property
    def __value(self) -> CommonGrid:
        points = self.__source.points
        n = len(self.__source.points)
        return CommonGrid(
            [points[0]]
            + [(points[i] + points[i-1]) / 2 for i in range(1, n)]
            + [points[n-1]]
        )
