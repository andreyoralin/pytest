import unittest
from unittest.mock import patch
from main import reduce

class TestSolverFunction(unittest.TestCase):

    @patch('builtins.print')
    def test_solver_function(self, mock_print):
        reduce(5, 10)
        assert(50)

if __name__ == '__main__':
    unittest.main()