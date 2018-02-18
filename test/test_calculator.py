import unittest
from app.calculator import Calculator

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,3)
        self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()
