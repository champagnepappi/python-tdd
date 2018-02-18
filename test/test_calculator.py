import unittest

class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calculator = Calculator()
        result = calc.add(2,3)
        self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()
