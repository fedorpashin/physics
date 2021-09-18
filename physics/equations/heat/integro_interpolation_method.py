from physics.equations.heat.heat_equation_algorithm import HeatEquationAlgorithm
from physics.equations.heat.heat_equation import HeatEquation

from final_class import final
from overrides import overrides

__all__ = ['IntegroInterpolationMethod']


@final
class IntegroInterpolationMethod(HeatEquationAlgorithm):
    @overrides
    def solution(self, equation: HeatEquation):
        # @todo #4:240min Implement integro-interpolation method
        raise NotImplementedError()
