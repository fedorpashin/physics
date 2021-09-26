from abc import abstractmethod

from physics.grids.any_grid import AnyGrid
from multimethod import multimethod


class AnyUniformGrid(AnyGrid):
    @abstractmethod
    @multimethod
    def h(self, i: int) -> float:
        pass

    @abstractmethod  # type: ignore
    @h.register
    def h(self) -> float:
        pass
