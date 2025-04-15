import unittest
from calculator import *

# https://github.com/marley-torres/lab10-MT-MT/tree/main
# Partner 1: Marley Torres
# Partner 2: Marley's second github account

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,1), 1)
        self.assertEqual(add(-1,4), 3)
        self.assertEqual(add(1.2,2.1), 3.3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,2), 3)
        self.assertEqual(subtract(-3,2),-5)
        self.assertEqual(subtract(0,4), -4)
    ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(4, 32), 5/2)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1/25), -2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-10, 100)
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()