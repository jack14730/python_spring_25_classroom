'''
while loop demonstration

'''
# first i entered the count at 0, then i have the beer to equal 99
count = 0
beer = 99
# I use a while statement to let it count down from 98
while count <= 98:
    if beer > 1:
        print(f"{beer} bottles of beer on the wall!")
        print(f"{beer} bottles of beer!")
    else:
        print(f"{beer} bottle of beer on the wall!")
        print(f"{beer} bottle of beer!")
# Then I have the elif statement and else statement for when the terminal reaches 0
    beer -= 1
    print("Take one down, pass it around")
    if beer > 1:
        print(f"{beer} bottles of beer on the wall!")
    elif beer == 1:
        print(f"{beer} bottle of beer on the wall!")
    else:
        print("No more bottles of beer on the wall!")

    print("\n")
    count += 1
