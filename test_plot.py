import unittest
import plot
from datetime import datetime


class Test_string_to_datetime(unittest.TestCase):

    def test_basic(self):
        dt = plot.string_to_datetime('2021-11-20 18:00:00')
        self.assertEqual(dt, datetime(year=2021, month=11, day=20, hour=18, minute=0, second=0))
