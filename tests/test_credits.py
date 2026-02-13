import unittest

class TestCreditCalculations(unittest.TestCase):

    def test_basic_credit(self):
        self.assertEqual(calculate_credit(100), 15)  # Sample calculation

    def test_gradual_credit(self):
        self.assertEqual(calculate_credit(200), 30)  # Sample calculation

    def test_high_income_credit(self):
        self.assertEqual(calculate_credit(1000), 5)  # Sample calculation

if __name__ == '__main__':
    unittest.main()