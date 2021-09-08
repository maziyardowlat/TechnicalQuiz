import unittest
import AngleCalc


class TestCalc(unittest.TestCase):

    def test_angle(self):
        result = AngleCalc.boundTo180(10)
        self.assertEqual(result, 10)

    def test_cases(self):
        result = AngleCalc.isAngleBetween(10, 1, 5)
        self.assertTrue((10, 1, 5))
