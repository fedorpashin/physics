from physics.grids.any_grid import AnyGrid

from abc import abstractmethod

__all__ = ['AnyAuxiliaryGrid']


class AnyAuxiliaryGrid(AnyGrid):
    @abstractmethod
    def point_with_half(self, i: int) -> float:
        pass
