from linalg import Vector
from physics.equations.any_equation import AnyEquation

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

__all__ = ['AnyAlgorithm']

T = TypeVar('T', bound=AnyEquation)


class AnyAlgorithm(ABC, Generic[T]):
    @abstractmethod
    def solution(self, equation: T) -> Vector:
        pass
