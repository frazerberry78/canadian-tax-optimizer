def calculate_federal_tax_credit(income):
    # Example federal tax credit calculations based on income
    if income <= 50000:
        return income * 0.15  # 15% for example
    elif income <= 100000:
        return 50000 * 0.15 + (income - 50000) * 0.2  # 20% on the amount over 50k
    else:
        return 50000 * 0.15 + (100000 - 50000) * 0.2 + (income - 100000) * 0.25  # 25% on the amount over 100k


def calculate_provincial_tax_credit(income, province):
    # Example provincial tax credit calculations based on province and income
    # This is a placeholder; you'd replace with real provincial rates
    provincial_rates = {
        'Ontario': 0.05,
        'Quebec': 0.06,
        'British Columbia': 0.045,
        'Alberta': 0.04,
    }
    rate = provincial_rates.get(province, 0.05)  # Default rate if province not found
    return income * rate


# Example usage:
if __name__ == '__main__':
    income = 75000  # Example income
    province = 'Ontario'
    federal_credit = calculate_federal_tax_credit(income)
    provincial_credit = calculate_provincial_tax_credit(income, province)
    print(f'Federal Tax Credit: {federal_credit}')
    print(f'Provincial Tax Credit: {provincial_credit}')