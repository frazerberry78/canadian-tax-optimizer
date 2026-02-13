def calculate_tax(income, tax_brackets):
    """
    Calculate the total tax owed based on the income and tax brackets.

    :param income: The total income of the individual.
    :param tax_brackets: A list of tuples containing (income_limit, tax_rate).
    :return: Total tax owed.
    """
    total_tax = 0.0
    previous_limit = 0

    for limit, rate in tax_brackets:
        if income > limit:
            taxable_income = limit - previous_limit
            total_tax += taxable_income * rate
            previous_limit = limit
        else:
            taxable_income = income - previous_limit
            total_tax += taxable_income * rate
            break

    return total_tax

# Example usage:
income = 75000
# Example tax brackets: [(50000, 0.15), (100000, 0.2)]
tax_brackets = [(50000, 0.15), (100000, 0.2)]
total_tax = calculate_tax(income, tax_brackets)
print(f'Total tax owed: ${total_tax:.2f}')