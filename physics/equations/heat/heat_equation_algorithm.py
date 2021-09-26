import linalg as la
from physics.equations.any_algorithm import AnyAlgorithm
from physics.equations.heat.heat_equation import HeatEquation
from physics.grids.default_grid import DefaultGrid
from physics.grids.any_grid import AnyGrid

from abc import abstractmethod
from multimethod import multimethod
from overrides import overrides

__all__ = ['HeatEquationAlgorithm']


class HeatEquationAlgorithm(AnyAlgorithm):
    @multimethod
    @abstractmethod
    def solution(self, equation: HeatEquation, grid: AnyGrid) -> la.Solution:
        pass

    @solution.register  # type: ignore
    @overrides
    def solution(self, equation: HeatEquation) -> la.Solution:
        return self.solution(equation, DefaultGrid(equation))
