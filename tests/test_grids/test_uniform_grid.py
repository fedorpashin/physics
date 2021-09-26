from physics.grids.uniform_grid import UniformGrid
from physics import Interval

from typing import Final

import unittest
from numpy.testing import assert_almost_equal


class TestUniformGrid(unittest.TestCase):
    interval: Final = Interval(1, 5)
    num_parts: Final = 4
    grid: Final = UniformGrid(interval, num_parts)

    def test_points(self):
        assert_almost_equal(self.grid.points, [1, 2, 3, 4, 5])

    def test_point(self):
        self.assertEqual(self.grid.point(2), 3)

    def test_interval(self):
        self.assertEqual(self.grid.interval, self.interval)

    def test_num_parts(self):
        self.assertEqual(self.grid.num_parts, self.num_parts)

    def test_h(self):
        self.assertEqual(self.grid.h(2), 1)

    def test_h_without_index(self):
        self.assertEqual(self.grid.h(), 1)
