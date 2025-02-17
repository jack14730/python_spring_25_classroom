'''
Accept a numeric grade from the user and display a letter grade. 

The  grading scale is:  
90-100: A 
80-89: B 
70-79: C 
60-69: D 
Below 60: F

Check to see if the number given is between 0 and 100.  
'''

# prompt question to ask user for their grade number.
grade = int(input("Enter your numeric grade:"))


# if grade below 60 user letter grade is F
# if grade 60-69 user letter grade is D
if grade < 60:
    print("The letter grade is: F")

elif grade <= 69:
    print("The letter grade is: D")


# if grade is 70-79 user letter grade is C
if grade < 70:
    print("The letter grade is: D")

elif grade <= 79:
    print("The letter grade is: C")


# if grade is 80-89 user letter grade is B
if grade < 80:
    print("The letter grade is: C")

elif grade <= 89:
    print("The letter grade is: B")


# if grade is 90-100 user letter grade is A

elif grade <= 100:
    print("The letter grade is: A")
