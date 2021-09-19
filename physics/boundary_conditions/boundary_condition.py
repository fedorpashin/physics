from abc import ABC, abstractmethod

__all__ = ['BoundaryCondition']


class BoundaryCondition(ABC):
    @property
    @abstractmethod
    def ν(self):
        pass
