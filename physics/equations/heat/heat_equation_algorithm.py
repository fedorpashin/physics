from physics.equations.any_algorithm import AnyAlgorithm
from physics.equations.heat.heat_equation import HeatEquation

from abc import abstractmethod

__all__ = ['HeatEquationAlgorithm']


class HeatEquationAlgorithm(AnyAlgorithm):
    @abstractmethod
    def solution(self, equation: HeatEquation):
        pass
