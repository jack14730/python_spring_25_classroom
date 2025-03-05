"""
    Enhance a basic Python program by implementing try and except statements to handle errors in user input,
     focusing on data type errors.
"""

# Simple Python program to calculate the square of a number


def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Please check your input, that was not valid.")
    except Exception as e:
        print(f"You had an {e} error.")
    finally:
        print("Goodbye!")


square_number()
