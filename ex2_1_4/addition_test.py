import addition
import unittest

# addition only contains test code. Its entry point executes all tests
# to check that the library functions are implemented correctly.

class TestAddition(unittest.TestCase):
    
    def test_basic(self):
        input_a= [1, 1, 1, 1, 1, 1, 0, 1]
        input_b= [0, 0, 0, 0, 1, 1, 0, 1]
        output_number= addition.add(input_a, input_b)    
        expected_number = [1, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(output_number,expected_number)
        
        
if __name__== '__main__':
    unittest.main()
