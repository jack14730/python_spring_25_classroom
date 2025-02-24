"""
    Create a Python script to track heart rate readings and calculate the average heart rate.

    Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").

    Use a loop to prompt the user for heart rate (in BPM) at each time slot.

    Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.

    Calculate the average heart rate and display it.

    """

# variables
heart_rate_times = ["Morning", "Midday", "Afternoon", "Evening"]

correct_number = 100

heart_rate_with_times = []

total = 0

# get info from user
for time in heart_rate_times:
    heart_rate = int(input(f"Please enter the {time} heart rate level: "))
    while heart_rate > 200 or heart_rate < 30:
        correct_number = input(
            f"The rate {heart_rate} is outside of normal ranges. Are you sure? (Y or N)")
        if correct_number == "Y" or correct_number == "y":
            break
        else:
            heart_rate = int(
                input(f"Please enter the {time} heart rate level: "))
heart_rate_times.append([time, heart_rate])
print(heart_rate_with_times)

# print(heart_rate_with_times)

# print results to screen

for item in range(len(heart_rate_with_times)):
    print(
        f"For {heart_rate_with_times[item][0]} the heart rate was {heart_rate_with_times[item][1]}")


# calculate average and print to screen
total += heart_rate_with_times[item][1]

average = total / len(heart_rate_with_times)
print(f"Your average heart rate today was: {average:,.1f}")
