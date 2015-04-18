import addition
import unittest

# addition only contains test code. Its entry point executes all tests
# to check that the library functions are implemented correctly.

class TestAddition(unittest.TestCase):
    
    def test_basic(self):
        input_a= [1, 1, 1, 1, 1, 1, 0, 1]
        input_b= [0, 0, 0, 0, 1, 1, 0, 1]
        output_number_add= addition.add(input_a, input_b)
        output_number_imp_add=addition.imp_add(input_a,input_b)    
        expected_number = [1, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(output_number_add,expected_number)
        self.assertEqual(output_number_imp_add,expected_number)
        
        # NOTE(orlov) the problem statement does not say that the high
        # order bit must be set to one. For example, zero is a perfect
        # n-bit integer, for any n.
        # Could you add some tests that add numbers where top bit is
        # zero?
        
if __name__== '__main__':
    unittest.main()
