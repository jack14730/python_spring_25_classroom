"""
    Write a Python function named calculate_interest that computes and returns simple interest based on given parameters.
"""


def main():
    principal, rate, time = get_values()
    simple_interest = calculate_interest(principal, rate, time)
    print(
        f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${simple_interest:,.2f}.")


def get_values():
    principal = float(input("Please enter the principal amount: "))
    rate = float(input("Please enter the interest rate: "))
    time = float(input("Please enter the time in years: "))
    return principal, rate, time


def calculate_interest(principal, rate, time):
    simple_interest = principal * rate * time / 100
    return simple_interest


main()
