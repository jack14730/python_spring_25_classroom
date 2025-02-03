'''
    Create a Python application that allows users to input their total budget and the amount spent in various categories. The program will then calculate and display the percentage of the total budget each category represents.
    Requirements:
    Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
    Housing (rent or mortgage)
    Utilities
    Groceries
    Transportation
    Health Care
    Personal Care
    Clothing
    Debt
    Calculate the percentage of the total budget spent in each category.
    Display the results in a user-friendly format using f-strings.
    Ensure your code is well-commented to explain the functionality of different sections.
'''

"""
    _summary_
        Calculator used to breakdown users budgets to help see how it is allocated through different categories.
"""

#     # variables
# total budget = 95000
# net monthly income = 5780
# money to spend: 2890  # money amount set aside to use for needs
# rent = 1944  # rent per month
# utilities = 335  # utility cost per month
# groceries = 327.31
# transportation = 441.67
# health care = 279.49
# personal care =
# clothing = 120
# debt = 719

# Get input from user
budget = float(input("budget: 5780 "))
rent = float(input(" rent per month: 1944 "))
utilities = float(input(" utilities per month: 335 "))
groceries = float(input(" groceries cost per month: 327.31 "))
transportation = float(input(" transportation cost per month: 441.67 "))
health_care = float(input(" health care per month: 279.49 "))
clothing = float(input(" clothing per month: 120 "))
debt = float(input("debt per month: 719"))

# calculations

rent_percent = budget/rent * 100
utilities_percent = budget/utilities * 100
groceries_percent = budget/groceries * 100
transportation_percent = budget/transportation * 100
health_care_percent = budget/health_care * 100
clothing_percent = budget/clothing * 100
debt_percent = budget/debt * 100

# total budget spent

print(f"Your housing is %{rent_percent:.1f} of your monthly budget.")
print(f"Your housing is %{utilities_percent:.1f} of your monthly budget.")
print(f"Your housing is %{groceries_percent:.1f} of your monthly budget.")
print(f"Your housing is %{transportation_percent:.1f} of your monthly budget.")
print(f"Your housing is %{health_care_percent:.1f} of your monthly budget.")
print(f"Your housing is %{clothing_percent:.1f} of your monthly budget.")
print(f"Your housing is %{debt_percent:.1f} of your monthly budget.")

# Money left after expenses
