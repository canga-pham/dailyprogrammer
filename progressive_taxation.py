from math import floor

TAXATION_RULE = [(0, 0), (10000, 0.1), (30000, 0.25), (100000, 0.4)]


def taxation(income, taxation_rule):
    taxation_rule.sort()
    tax_amount = 0
    for tax_class, tax in reversed(taxation_rule):
        if income > tax_class:
            income_tax = income - tax_class
            tax_amount += income_tax*tax
            income = tax_class
    return floor(tax_amount)

