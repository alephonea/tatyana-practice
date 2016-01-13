#!/usr/bin/python

import solution
import unittest

# solution_test only contains test code. Its entry point executes all tests
# to check that the library functions are implemented correctly.

class TestFibonacci(unittest.TestCase):

    def test_basic(self):
        input_number= 18
        output_number= solution.fibonacci(input_number)
        expected_number = 4181
        self.assertEqual(output_number,expected_number)


if __name__== '__main__':
    unittest.main()


