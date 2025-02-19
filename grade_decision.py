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


# I had revised the code in order to make the input not output multiple letter grades.
if grade < 60:
    print("The letter grade is: F")

elif grade < 70:
    print("The letter grade is: D")

elif grade < 80:
    print("The letter grade is: C")

elif grade < 90:
    print("The letter grade is: B")

elif grade <= 100:
    print("The letter grade is: A")

else:
    print("This numeric grade is invalid.")
# I had also incorporated a else statement in order to make sure that invalid number grades do not show up as a letter grade.
