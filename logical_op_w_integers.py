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
num2 = int(input("Enter another integer:"))

# and operator
if num1 and num2 > 0:
    print("Both numbers are greater than 0: True")

else:
    print("Both numbers are greater than 0: False")

if num1 and num2 > 100:
    print("Both numbers are greater than 100: True")

else:
    print("Both numbers are greater than 100: False")

# or operator
if num1 or num2 < 100:
    print("Either number is less than 100? True")
else:
    print("Either number is less than 100? False")

if num1 or num2 % 2 == 0:
    print("Either number is even? True")
else:
    print("Either number is even? False")

# not operator. For this portion i have incorporated a f strings so that it will output the users integers they have written.
if not num1 > num2:
    print(f"{num1} is not greater than {num2}")
else:
    print(f"{num1} is greater than {num2}")

if not num1 == num2:
    print(f"{num1} is not equal to {num2}: True")
else:
    print(f"{num1} is not equal to {num2}: False")
