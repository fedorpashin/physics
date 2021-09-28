from physics.equations.heat.heat_equation_algorithm import HeatEquationAlgorithm
from physics.equations.heat.heat_equation import HeatEquation
from physics.grids.any_grid import AnyGrid
from physics.boundary_conditions.first_type_boundary_condition import FirstTypeBoundaryCondition
from physics.boundary_conditions.second_type_boundary_condition import SecondTypeBoundaryCondition

import linalg as la

from dataclasses import dataclass
from final_class import final
from overrides import overrides
from undefined import Undefined

__all__ = ['IntegroInterpolationMethod']


@final
@dataclass(frozen=True)
class IntegroInterpolationMethod(HeatEquationAlgorithm):
    @overrides
    def solution(self, equation: HeatEquation, grid: AnyGrid) -> la.Solution:
        FirstType = FirstTypeBoundaryCondition
        SecondType = SecondTypeBoundaryCondition

        # k = equation.k
        # q = equation.q
        # f = equation.f
        lbc = equation.left_boundary_condition
        rbc = equation.right_boundary_condition
        n = grid.n

        # @todo #8:60min Fill in the gaps
        return la.Solution(
            la.System(
                la.TridiagonalMatrix(
                    a = [
                        Undefined for i in range(n)
                    ] + [
                        0 if type(rbc) is FirstType else
                        -1 if type(rbc) is SecondType else  # noqa
                        Undefined
                    ],
                    b = [
                        0 if type(lbc) is FirstType else
                        Undefined if type(lbc) is SecondType else
                        Undefined
                    ] + [
                        None for i in range(n)
                    ],
                    c = [
                        1 if type(lbc) is FirstType else
                        Undefined if type(lbc) is SecondType else
                        Undefined
                    ] + [
                        Undefined for i in range(n)
                    ] + [
                        1 if type(rbc) is FirstType else
                        Undefined if type(rbc) is SecondType else
                        Undefined
                    ]
                ),
                la.Vector(
                    [lbc.ν] + [0 for i in range(n)] + [rbc.ν]
                )
            )
        )
