from linalg import AnyVector
from physics.equations.any_equation import AnyEquation
from physics.equations.any_algorithm import AnyAlgorithm
from physics.factories.default_algorithm import DefaultAlgorithm

from dataclasses import dataclass
from typing import TypeVar
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['Solution']

T = TypeVar('T', bound=AnyEquation)


@final
@dataclass
class Solution(AnyVector):
    __equation: T  # type: ignore
    __algorithm: AnyAlgorithm[T]

    def __init__(self, equation: T, algorithm: AnyAlgorithm[T] = None):
        self.__equation = equation
        self.__algorithm = DefaultAlgorithm(self.equation) if algorithm is None else algorithm

    @cached_property  # type: ignore
    @overrides
    def value(self) -> list[float]:
        return self.algorithm.solution(self.equation).value

    @property
    def equation(self):
        return self.__equation

    @property
    def algorithm(self):
        return self.__algorithm

    def __repr__(self):
        return self.value.__repr__()
