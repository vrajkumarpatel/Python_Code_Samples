# Vrajkumar Patel
# 10/26/2025
# What the program does: Iterates through a given list of numbers to print each number,
# then iterates again to print each number and its square.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# 1. Loop to print each number on a new line
print("--- Printing Each Number ---")
for number in numbers:
    print(number)

# 2. Loop to print each number and its square on a new line
print("\n--- Printing Number and Square ---")
for number in numbers:
    square = number ** 2 # Use the exponentiation operator
    print(f"Number: {number}, Square: {square}")