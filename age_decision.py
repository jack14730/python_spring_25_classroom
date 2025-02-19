'''
    Write a Python program that uses if-else statements age:
    
    Asks the user for their age and converts the input to an integer.
    Check to see if the user is old enough to drive.
    Check to see if the user can vote.
    Check to see if the user can legally buy alcohol.
    Check to see if the user is eligible for a senior discount.
    Print all the results on the screen, ensuring the output is straightforward and user friendly.

    Remember:

    Comment your code to explain the functionality of each section.
    Handle edge cases, such as ages, precisely at the thresholds.    
'''
# prompt Question for user to input their Age as an integer
age = int(input("How old are you:"))


# if person is or is not allowed to Drive it will show these
if age <= 16:
    print("You are not eligible to have a drivers license.")
    # ^ if the user puts less than or equal to 15 they will not be allowed to do anything asked on the list

else:
    print("You are eligible to have a drivers license.")


# if person is or is not allowed to Vote
if age < 18:
    print("You cannot legally vote.")
    # ^ if the user is less than or equal to 17 they will only be allowed to drive but it will list what they cannot do

else:
    print("You can legally vote.")


# if person is or is not allowed to purchase and Drink Alcohol
if age < 21:
    print("You are not the legal drinking age.")

else:
    print("You are the legal drinking age.")


# if person is or is not allowed for Senior Discount
if age < 65:
    print("You are not eligible for a senior discount. ")

else:
    print("You are eligible for a senior discount!")
