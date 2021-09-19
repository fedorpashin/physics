from physics.grids.uniform_grid import UniformGrid
from physics import Interval

from typing import Final

import unittest
from numpy.testing import assert_almost_equal


class TestUniformGrid(unittest.TestCase):
    interval: Final = Interval(1, 5)
    n: Final = 4
    grid: Final = UniformGrid(interval, n)

    def test_points(self):
        assert_almost_equal(self.grid.points, [1, 2, 3, 4, 5])

    def test_point(self):
        self.assertEqual(self.grid.point(2), 3)

    def test_interval(self):
        self.assertEqual(self.grid.interval, self.interval)

    def test_n(self):
        self.assertEqual(self.grid.n, self.n)

    def test_h(self):
        self.assertEqual(self.grid.h, 1)
