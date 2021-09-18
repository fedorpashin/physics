from physics.equations.heat.heat_equation import HeatEquation
from physics.equations.heat.heat_equation_algorithm import HeatEquationAlgorithm
from physics.equations.heat.default_heat_equation_algorithm import DefaultHeatEquationAlgorithm

from multimethod import multimeta
from final_class import final

__all__ = ['DefaultAlgorithm']


@final
class DefaultAlgorithm(metaclass=multimeta):
    def __new__(cls, equation: HeatEquation) -> HeatEquationAlgorithm:
        return DefaultHeatEquationAlgorithm()
