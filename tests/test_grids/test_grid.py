from physics.grids.grid import Grid
from physics import Interval

from typing import Final

import unittest


class TestGrid(unittest.TestCase):
    points: Final = [1, 1.2, 1.5, 2, 3]
    grid: Final = Grid(points)

    def test_points(self):
        self.assertEqual(self.grid.points, self.points)

    def test_point(self):
        self.assertEqual(self.grid.point(3), 2)

    def test_interval(self):
        self.assertEqual(self.grid.interval, Interval(1, 3))

    def test_n(self):
        self.assertEqual(self.grid.n, 4)
