from physics.grids.common_auxiliary_grid import CommonAuxiliaryGrid
from physics.grids.common_grid import CommonGrid
from physics import Interval

from typing import Final

import unittest


class TestCommonAuxiliaryGrid(unittest.TestCase):
    grid: Final = CommonAuxiliaryGrid(
        CommonGrid([1, 1.2, 1.5, 2, 3])
    )

    def test_points(self):
        self.assertEqual(self.grid.points, [1, 1.1, 1.35, 1.75, 2.5, 3])

    def test_point(self):
        self.assertEqual(self.grid.point(3), 2)

    def test_point_with_half(self):
        self.assertEqual(self.grid.point(3, with_half=True), 2.5)

    def test_interval(self):
        self.assertEqual(self.grid.interval, Interval(1, 3))

    def test_num_parts(self):
        self.assertEqual(self.grid.num_parts, 5)

    def test_h(self):
        self.assertAlmostEqual(self.grid.h(2), 0.4)
