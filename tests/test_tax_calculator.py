import unittest
from tax_calculator import calculate_tax  # Assuming tax_calculator.py is in the same directory

class TestTaxCalculator(unittest.TestCase):
    def test_calculate_tax(self):
        # Test case 1: Check tax for income of $50,000
        self.assertEqual(calculate_tax(50000), 7500)  # Example tax calculation

        # Test case 2: Check tax for income of $100,000
        self.assertEqual(calculate_tax(100000), 15000)  # Example tax calculation

        # Test case 3: Check tax for income of $150,000
        self.assertEqual(calculate_tax(150000), 22500)  # Example tax calculation

if __name__ == '__main__':
    unittest.main()