"""



"""

# Bubble Sort to sort a list of names
names = []

# Ask user for input


swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True  # Mark that a swap occurred
print(names)


# Reverse the sorted list
names.reverse()
print(names)  # Reversed: ['ted', 'carol', 'bob', 'anna', 'alice']
