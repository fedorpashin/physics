from physics.grids.any_uniform_grid import AnyUniformGrid
from physics.grids.any_auxiliary_grid import AnyAuxiliaryGrid
from physics.grids.uniform_grid import UniformGrid
from physics import Interval

from dataclasses import dataclass
from multimethod import multimethod
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['UniformAuxiliaryGrid']


@final
@dataclass
class UniformAuxiliaryGrid(AnyUniformGrid, AnyAuxiliaryGrid):
    __source: AnyUniformGrid

    def __init__(self, grid: AnyUniformGrid):
        self.__source = grid

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return (
            [self.__source.interval.l]
            + self.__core.points
            + [self.__source.interval.r]
        )

    @overrides
    def point(self, i: int, with_half=False) -> float:
        return (
            self.__half_of_h + i*self.h() if with_half else
            self.__source.point(i)
        )

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.__source.interval

    @property  # type: ignore
    @overrides
    def num_parts(self) -> int:
        return self.__core.num_parts + 2

    @multimethod
    @overrides
    def h(self, i: int) -> float:
        return (
            self.__half_of_h if i == 0 or i == self.__source.num_parts else
            self.h()
        )

    @h.register  # type: ignore
    def h(self) -> float:
        return self.__core.h()

    @cached_property
    def __core(self) -> UniformGrid:
        interval = self.__source.interval
        num_parts = self.__source.num_parts
        return UniformGrid(
            Interval(interval.l + self.__half_of_h, interval.r - self.__half_of_h),
            num_parts - 1
        )

    @cached_property
    def __half_of_h(self) -> float:
        return self.__source.h() / 2
