import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-2,3),1)
        self.assertEqual(self.calc.add(-2,-3),-5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-5,-10),5)

    
    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, 4), -8)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333333333333335)
        self.assertEqual(self.calc.divide(5, 0), None) 
        self.assertEqual(self.calc.divide(0, 5), 0)

