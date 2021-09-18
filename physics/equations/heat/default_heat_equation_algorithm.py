from physics.equations.heat.integro_interpolation_method import IntegroInterpolationMethod

from final_class import final

__all__ = ['DefaultHeatEquationAlgorithm']


@final
class DefaultHeatEquationAlgorithm:
    def __new__(cls):
        return IntegroInterpolationMethod()
