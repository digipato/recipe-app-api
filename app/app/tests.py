"""
Sample tests.
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_numbers(self):
        """ Test adding numbers together. """
        res = calc.add(6, 6)

        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """ Test subtracting numbers. """
        res = calc.subtract(10, 15)

        self.assertEquals(res, 5)
