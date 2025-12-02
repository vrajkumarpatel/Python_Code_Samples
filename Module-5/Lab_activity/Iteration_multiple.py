# Vrajkumar Patel
# 10/26/2025
# Program: Prints numbers 1-50, with special messages for multiples of 3, 5, or both

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")  # Hits multiples of 15 first
    elif num % 3 == 0:
        print("Divisible by three")
    elif num % 5 == 0:
        print("Divisible by five")
    else:
        print(num)  # Just the number if nothing special
