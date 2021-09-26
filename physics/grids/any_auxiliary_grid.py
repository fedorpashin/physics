from abc import ABC, abstractmethod

__all__ = ['AnyAuxiliaryGrid']


class AnyAuxiliaryGrid(ABC):
    @abstractmethod
    def point_with_half(self, i: int) -> float:
        pass
