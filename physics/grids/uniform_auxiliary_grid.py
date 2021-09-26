from physics.grids.any_uniform_grid import AnyUniformGrid
from physics.grids.any_auxiliary_grid import AnyAuxiliaryGrid
from physics.grids.uniform_grid import UniformGrid
from physics import Interval

from multimethod import multimethod
from overrides import overrides

from functools import cached_property

__all__ = ['UniformAuxiliaryGrid']


class UniformAuxiliaryGrid(AnyUniformGrid, AnyAuxiliaryGrid):
    source: AnyUniformGrid

    def __init__(self, grid: AnyUniformGrid):
        self.source = grid

    @property  # type: ignore
    @overrides
    def points(self) -> list[float]:
        return (
            [self.source.interval.l]
            + self.__core.points
            + [self.source.interval.r]
        )

    @overrides
    def point(self, i: int) -> float:
        return (
            self.interval.l
            + (self.__half_of_h if i > 0 else 0)
            + ((i-1) * self.h() if i > 1 else 0)
        )

    @property  # type: ignore
    @overrides
    def interval(self) -> Interval:
        return self.source.interval

    @property  # type: ignore
    @overrides
    def n(self) -> int:
        return self.__core.n + 2

    @multimethod
    @overrides
    def h(self, i: int) -> float:
        return self.__core.h(i)

    @h.register  # type: ignore
    def h(self) -> float:
        return self.__core.h()

    @overrides
    def point_with_half(self, i: int) -> float:
        return self.point(i+1)

    @cached_property
    def __core(self) -> UniformGrid:
        interval = self.source.interval
        n = self.source.n
        return UniformGrid(
            Interval(interval.l + self.__half_of_h, interval.r - self.__half_of_h),
            n - 1
        )

    @cached_property
    def __half_of_h(self) -> float:
        return self.source.h() / 2
