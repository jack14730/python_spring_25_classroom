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

# i am using this so I have numbers to type in for the inputs

# total budget = 95000
# net monthly income = 5780
# money to spend = 2890  # money amount set aside to use for needs
# rent = 1944  # rent per month
# utilities = 335  # utility cost per month
# groceries = 327.31
# transportation = 441.67
# health care = 279.49
# personal care =
# clothing = 120
# debt = 719

# Get input from user

budget = float(input("budget: "))
rent = float(input("rent per month: "))
utilities = float(input("utilities per month: "))
groceries = float(input("groceries cost per month: "))
transportation = float(input("transportation cost per month: "))
health_care = float(input("health care per month: "))
clothing = float(input("clothing per month: "))
debt = float(input("debt per month: "))
# this is to allow the user to input numbers into the terminal to allow the program to use those numbers for the calculations


# calculations

rent_percent = (rent / budget) * 100
utilities_percent = (utilities / budget) * 100
groceries_percent = (groceries / budget) * 100
transportation_percent = (transportation / budget) * 100
health_care_percent = (health_care / budget) * 100
clothing_percent = (clothing / budget) * 100
debt_percent = (debt / budget) * 100

# total budget spent

print(f"Your rent is %{rent_percent:.1f} of your monthly budget.")
print(f"Your utilities is %{utilities_percent:.1f} of your monthly budget.")
print(f"Your groceries is %{groceries_percent:.1f} of your monthly budget.")
print(f"Your transportation is %{
      transportation_percent:.1f} of your monthly budget.")
print(f"Your health_care is %{
      health_care_percent:.1f} of your monthly budget.")
print(f"Your clothing is %{clothing_percent:.1f} of your monthly budget.")
print(f"Your debt is %{debt_percent:.1f} of your monthly budget.")
# print of what your percentages will be for a monthly budget


# Money left after expenses

# calculates all of the expenses to give number of how much spent
expenses = (rent + utilities + groceries +
            transportation + health_care + clothing + debt)
leftover_funds = (budget - expenses)  # calculates how much is left over
# print of what you have left over after typing each expense in the terminal
print("Your leftover funds after expenses is: ", leftover_funds)
