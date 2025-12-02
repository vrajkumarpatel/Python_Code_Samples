# Vrajkumar Patel
# 11/23/2025
# Problem 3: Ask user for numbers until total sum is greater than 100

numbers = []      # List to store user-entered numbers
total = 0         # Running total

while total <= 100:   
    user_num = float(input("Enter a number: "))  # Get number from user
    numbers.append(user_num)                     # Store in list
    total += user_num                            # Add to total

print("Numbers entered:", numbers)
print("Total sum:", total)
