# Vrajkumar Patel
# 11/23/2025
# Problem 4: Append numbers divisible by 10 (0–50) into a list

tens = []        # List to hold numbers divisible by 10
counter = 0      # Start counter at 0

while counter <= 50:             # Loop until counter reaches 50
    if counter % 10 == 0:        # Check if divisible by 10
        tens.append(counter)
    counter += 1                 # Increase counter by 1

print("Numbers divisible by 10:", tens)
