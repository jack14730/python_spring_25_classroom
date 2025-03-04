"""
  
    Create a List: Start by creating a list named days that includes all seven days of the week.
   
    initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
   
    User Input: Using a loop, ask the user to enter the number of steps they took for each day.
    
    Store Steps: Append the user's input to the steps list.
    
    Display Daily Steps: Show the user the steps recorded for each day.
    
    Total Steps: Calculate and display the total number of steps taken in the week.
    
    Average Steps: Calculate and display the average steps.

"""

# variables

day = ["Sunday", "Monday", "Tuesday",
       "Wednesday", "Thursday", "Friday", "Saturday"]

steps = []

# getting user info

steps = int(input(f"How many steps did you take on {day}?: "))

for i in range(len(day)):
    day = day[i]
    steps = num_of_steps[i]
    print(f"{month} has {days} days")
