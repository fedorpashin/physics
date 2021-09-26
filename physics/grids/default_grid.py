from physics.grids.any_grid import AnyGrid
from physics.equations.any_equation import AnyEquation

__all__ = ['DefaultGrid']


class DefaultGrid(AnyGrid):
    # @todo #8:60min Implement default grid
    equation: AnyEquation

    def __init__(self, equation: AnyEquation):
        self.equation = equation
