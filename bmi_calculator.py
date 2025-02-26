"""
    Objective: Create a BMI calculator that takes a user's weight and height, 
    calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.

    REQUIREMENTS:
    
    Global Variables:
    Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).

    Main Function:
    Prompt the user for their weight in pounds and height in inches.
    Convert the inputs to metric units using global conversion constants.
    Calculate BMI using the formula bmi = weight / (height * height).
    Determine the BMI category based on standard ranges.
    Display the BMI value and category.

    Commenting:
    Include comments to explain key parts of the code.
"""

# global constant


def main():


    # here i am classifying what the weight and height will define.
weight, height = get_values()


def get_values():


weight = int(input("Please enter your weight in pounds: "))
height = int(input("Please enter your height in inches: "))

main()
