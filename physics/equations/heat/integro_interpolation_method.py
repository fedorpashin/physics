from physics.equations.heat.heat_equation_algorithm import HeatEquationAlgorithm
from physics.equations.heat.heat_equation import HeatEquation
from physics.grids.any_grid import AnyGrid
from physics.factories.auxiliary_grid import AuxiliaryGrid
from physics.boundary_conditions.first_type_boundary_condition import FirstTypeBoundaryCondition
from physics.boundary_conditions.third_type_boundary_condition import ThirdTypeBoundaryCondition

import linalg as la

from dataclasses import dataclass
from multimethod import multimethod
from final_class import final
from overrides import overrides
from undefined import Undefined

__all__ = ['IntegroInterpolationMethod']


@final
@dataclass(frozen=True)
class IntegroInterpolationMethod(HeatEquationAlgorithm):
    @multimethod
    @overrides
    def solution(self, equation: HeatEquation, grid: AnyGrid) -> la.Solution:
        FirstType = FirstTypeBoundaryCondition
        ThirdType = ThirdTypeBoundaryCondition

        h = grid.h
        n = grid.num_parts

        auxiliary_grid = AuxiliaryGrid(grid)  # type: ignore
        ħ = auxiliary_grid.h
        x = auxiliary_grid.point

        k = equation.k
        q = equation.q
        f = equation.f
        lbc = equation.left_boundary_condition
        rbc = equation.right_boundary_condition

        return la.Solution(
            la.System(
                la.TridiagonalMatrix(
                    a = [
                        -k(x(i-1, with_half=True)) / h(i)
                        for i in range(1, n)
                    ] + [
                        0
                            if isinstance(rbc, FirstType) else
                        -k(x(n-1, with_half=True)) / h(n)
                            if isinstance(rbc, ThirdType) else
                        Undefined
                    ],
                    b = [
                        0
                            if isinstance(lbc, FirstType) else
                        -k(x(0, with_half=True)) / h(1)
                            if isinstance(lbc, ThirdType) else
                        Undefined
                    ] + [
                        -k(x(i, with_half=True)) / h(i+1)
                        for i in range(1, n)
                    ],
                    c = [
                        1
                            if isinstance(lbc, FirstType) else
                        k(x(0, with_half=True)) / h(1) + lbc.κ + ħ(0) * q(x(0))
                            if isinstance(lbc, ThirdType) else
                        Undefined
                    ] + [
                        k(x(i-1, with_half=True)) / h(i) + k(x(i, with_half=True)) / h(i+1) + ħ(i) * q(x(i))
                        for i in range(1, n)
                    ] + [
                        1
                            if isinstance(rbc, FirstType) else
                        k(x(n-1, with_half=True)) / h(n) + rbc.κ + ħ(n) * q(x(n))
                            if isinstance(rbc, ThirdType) else
                        Undefined
                    ]
                ),
                la.Vector(
                    [
                        lbc.ν
                            if isinstance(lbc, FirstType) else
                        ħ(0) * f(x(0)) + lbc.ν
                            if isinstance(lbc, ThirdType) else
                        Undefined
                    ] + [
                        ħ(i) * f(x(i)) for i in range(1, n)
                    ] + [
                        rbc.ν
                            if isinstance(rbc, FirstType) else
                        ħ(n) * f(x(n)) + rbc.ν
                            if isinstance(rbc, ThirdType) else
                        Undefined
                    ]
                )
            )
        )
