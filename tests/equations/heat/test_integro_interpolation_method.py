from physics.equations.heat.integro_interpolation_method import IntegroInterpolationMethod
from physics.equations.heat.heat_equation import HeatEquation
from physics.grids.uniform_grid import UniformGrid
from physics.interval import Interval
from physics.boundary_conditions.first_type_boundary_condition import FirstTypeBoundaryCondition
from physics.boundary_conditions.third_type_boundary_condition import ThirdTypeBoundaryCondition

import unittest
from numpy.testing import assert_almost_equal


class TestIntegroInterpolationMethod(unittest.TestCase):
    def test_solution(self):
        for num_parts in [6, 12, 24]:
            with self.subTest():
                assert_almost_equal(
                    IntegroInterpolationMethod().solution(
                        HeatEquation(
                            interval=(interval := Interval(0, 2)),
                            k=lambda _: 1,
                            q=lambda _: 1,
                            f=lambda _: 1,
                            left_boundary_condition=FirstTypeBoundaryCondition(1),
                            right_boundary_condition=FirstTypeBoundaryCondition(1)
                        ),
                        grid := UniformGrid(
                            interval=interval,
                            num_parts=num_parts
                        )
                    ).value,
                    [1 for _ in grid.points]
                )

            with self.subTest():
                assert_almost_equal(
                    IntegroInterpolationMethod().solution(
                        HeatEquation(
                            interval=(interval := Interval(0, 2)),
                            k=lambda x: x**2 + 3,
                            q=lambda x: 10,
                            f=lambda x: 4*(x**2 + 11),
                            left_boundary_condition=FirstTypeBoundaryCondition(5),
                            right_boundary_condition=FirstTypeBoundaryCondition(9)
                        ),
                        grid := UniformGrid(
                            interval=interval,
                            num_parts=num_parts
                        )
                    ).value,
                    [x**2 + 5 for x in grid.points],
                    decimal=2
                )

            with self.subTest():
                assert_almost_equal(
                    IntegroInterpolationMethod().solution(
                        HeatEquation(
                            interval=(interval := Interval(0, 2)),
                            k=lambda x: x**2 - 2,
                            q=lambda x: 6,
                            f=lambda x: 22,
                            left_boundary_condition=ThirdTypeBoundaryCondition(3, 1),
                            right_boundary_condition=ThirdTypeBoundaryCondition(15, 1)
                        ),
                        grid := UniformGrid(
                            interval=interval,
                            num_parts=num_parts
                        )
                    ).value,
                    [x**2 + 3 for x in grid.points],
                    decimal=1
                )
