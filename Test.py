import unittest
from AngleCalc import AngleCalc

class TestCalc(unittest.TestCase):

    def test_angle(self):
        angle_calc = AngleCalc()
        result = angle_calc.boundTo180(10)
        result2 = angle_calc.boundTo180(-280)
        result3 = angle_calc.boundTo180(390)
        result4 = angle_calc.boundTo180(0)
        result5 = angle_calc.boundTo180(180)
        result6 = angle_calc.boundTo180(-180)
        self.assertEqual(result, 10)
        self.assertEqual(result2, 80)
        self.assertEqual(result3, 30)
        self.assertEqual(result4, 0)
        self.assertEqual(result5, 180)
        self.assertEqual(result6, 180)

    def test_cases(self):
        angle_calc = AngleCalc()
        result1 = angle_calc.isAngleBetween(3, 1, 2)
        result2 = angle_calc.isAngleBetween(0, 0 , 0)
        result3 = angle_calc.isAngleBetween(-90, -180, 110)
        result4 = angle_calc.isAngleBetween(-90, -180, 80)
        result5 = angle_calc.isAngleBetween(5, 6, 10)
        self.assertEqual(result2, False)
        self.assertEqual(result1, False)
        self.assertEqual(result3, True)
        self.assertEqual(result4, False)
        self.assertEqual(result5, True)
