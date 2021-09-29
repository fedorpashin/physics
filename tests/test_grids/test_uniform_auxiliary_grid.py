from physics.grids.uniform_auxiliary_grid import UniformAuxiliaryGrid
from physics.grids.uniform_grid import UniformGrid
from physics import Interval

from typing import Final

import unittest
from numpy.testing import assert_almost_equal


class TestUniformAuxiliaryGrid(unittest.TestCase):
    interval: Final = Interval(1, 5)
    grid: Final = UniformAuxiliaryGrid(
        UniformGrid(interval, 4)
    )

    def test_points(self):
        assert_almost_equal(self.grid.points, [1, 1.5, 2.5, 3.5, 4.5, 5])

    def test_point(self):
        self.assertEqual(self.grid.point(2), 3)

    def test_point_with_half(self):
        self.assertEqual(self.grid.point(2, with_half=True), 2.5)

    def test_interval(self):
        self.assertEqual(self.grid.interval, self.interval)

    def test_n(self):
        self.assertEqual(self.grid.n, 5)

    def test_h(self):
        self.assertEqual(self.grid.h(2), 1)

    def test_h_without_index(self):
        self.assertEqual(self.grid.h(), 1)
