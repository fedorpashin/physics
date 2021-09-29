from overrides import overrides

from physics.grids.any_grid import AnyGrid

from abc import abstractmethod

__all__ = ['AnyAuxiliaryGrid']


class AnyAuxiliaryGrid(AnyGrid):
    @abstractmethod
    def point(self, i: int, with_half=False) -> float:
        pass
