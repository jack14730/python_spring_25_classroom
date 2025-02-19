"""
    Practice using logical operators (and, or, not) in Python.
    Your task is to create a program that prompts the user for two integer inputs
    and then demonstrate the use of these operators 

    1. User Input: Start by asking the user to input two distinct integers
    2. Logical Operators: Implement six different logical comparisons using the input:
        and
        or
        not
    3. Display Results: Print the logical statement and its result for the each comparison.
    4. Guidelines for Logical Comparisons:
        Ensure that your comparisons are meaningful and not too obvious 
        (e.g., avoid comparisons like num1 == num1).
        Try to use comparisons that could yield different results based on user input.
    """

# Get input from user
num1 = int(input("Enter an integer:"))
num2 = int(input("Enter another integer: "))

# and operator

if num1 > 0 and num2 > 0:
    print("Both Numbers are greater than 0: True")
elif num1 < 100 and num2 < 100:
    print("Both Numbers are less than 100?: True")
