'''
Write a Python program to find and print all numbers divisible by 7 between 1 and 300. 
Use a for loop and the modulus operator (%).
'''

# I use a for loop statement to list the numbers in range of 1 to 301.
# then it has the % to show if the number is divisible by 7, lastly I added the print statement so that the number is shown on the terminal
for number in range(1, 301):
    if number % 7 == 0:
        print(number)
