'''
  Create a Python program that converts kilograms to pounds. 
    Use at least four different samples to convert. 
    A sample of the math is provided below; do not use the same 
    example in your program.

    Kilograms to Pounds Conversion:
    To convert kilograms (kg) to pounds (lb), use the formula:

    Pounds (lb) = Kilograms (kg) * 2.20462

    Example: 5 kg * 2.20462 = 11.0231 lb

'''
# c = 2.20462
# kilo = 150
# pound = kilo * c

# print(f"{kilo} kilograms = {pound: .1f} pounds")

# variables
kg_1 = 20
kg_2 = 45
kg_3 = 15
kg_4 = 30

conversion = 2.20462
lb_1 = kg_1 * conversion
lb_2 = kg_2 * conversion
lb_3 = kg_3 * conversion
lb_4 = kg_4 * conversion

print(f"{kg_1} Kilograms is equal to {lb_1:.2f} pounds")
print(f"{kg_2} Kilograms is equal to {lb_2:.2f} pounds")
print(f"{kg_3} Kilograms is equal to {lb_3:.2f} pounds")
print(f"{kg_4} Kilograms is equal to {lb_4:.2f} pounds")
