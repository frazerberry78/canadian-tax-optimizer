# Deductions Calculations and Utilities

def calculate_taxable_income(total_income, deductions):
    """Calculate taxable income after applying deductions."""
    return total_income - sum(deductions)


def calculate_deductions(deduction_items):
    """Calculate total deductions from a list of deduction items."""
    return [item['amount'] for item in deduction_items if 'amount' in item]


def main():
    # Example usage
    total_income = 50000  # Example total income
    deductions = calculate_deductions([{'name': 'RRSP', 'amount': 5000}, {'name': 'Charitable Donation', 'amount': 200}])
    taxable_income = calculate_taxable_income(total_income, deductions)
    print(f'Taxable Income: {taxable_income}')


if __name__ == '__main__':
    main()