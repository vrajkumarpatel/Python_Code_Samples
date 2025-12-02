# Vrajkumar Patel
# November 16, 2025
# Problem 4: Checks if a given year is a leap year.

def is_leap_year(year):
    """
    Takes a year and returns True if it is a leap year, False otherwise.
    Leap year rules: divisible by 4, 
                     UNLESS divisible by 100, 
                     UNLESS also divisible by 400.
    """
    # Check if the year is divisible by 400
    if (year % 400 == 0):
        return True
    # Check if the year is divisible by 100 (and NOT by 400, due to the first check)
    elif (year % 100 == 0):
        return False
    # Check if the year is divisible by 4 (and NOT by 100/400)
    elif (year % 4 == 0):
        return True
    # If none of the above are true, it's not a leap year
    else:
        return False

# Test the function
print(f"2000 is a leap year: {is_leap_year(2000)}")  # Divisible by 400 -> True
print(f"1900 is a leap year: {is_leap_year(1900)}")  # Divisible by 100, not 400 -> False
print(f"2024 is a leap year: {is_leap_year(2024)}")  # Divisible by 4, not 100 -> True
print(f"2023 is a leap year: {is_leap_year(2023)}")  # Not divisible by 4 -> False