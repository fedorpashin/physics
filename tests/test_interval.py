from physics.interval import Interval

import unittest


class TestInterval(unittest.TestCase):
    def test_invalid_interval(self):
        with self.subTest():
            with self.assertRaises(AssertionError):
                Interval(5, 4)
        with self.subTest():
            with self.assertRaises(AssertionError):
                Interval(4, 4)
