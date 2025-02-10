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

# if person is below this grade % then they are failing
if grade < 60:
    print("The letter grade is: F")

elif grade >= 60:
    print("The letter grade is: D")
