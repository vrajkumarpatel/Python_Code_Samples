# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 2: Check Range
# Description: Write a Python function to check whether a number is in a given range.
# Requirement: Use range(1,10) and print whether the number is in or not in the range.


def in_range(n: int, r=range(1, 10)) -> bool:
    """Return True if n is inside the given range (default 1..9 inclusive)."""
    return n in r


def main():
    # Prompt the user for an integer and report whether it's within 1..9
    try:
        n = int(input("Enter an integer to check if it's in range 1..9: "))
        if in_range(n):
            print(f"{n} is in the range 1..9.")
        else:
            print(f"{n} is NOT in the range 1..9.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()