#https://github.com/emailsuryaramesh-web/lab11-SR-VS.git
#Surya Ramesh
#Vennela Sadineni
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 1), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(4, 0), 4)
        self.assertEqual(subtract(-1, -1), 0)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-1,-1), 1)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(20, 2), 10)
        self.assertEqual(div(-6, -1), 6)
        self.assertEqual(div(5, 5), 1)
    ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3,1), 0)
        self.assertAlmostEqual(logarithm(3,9), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(10,0)
    ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(6,8), 10)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(36), 6)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()