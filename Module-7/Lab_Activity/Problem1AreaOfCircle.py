# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 1: Area of Circle
# Description: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Requirement: Use the math module.

import math


def areaOfCircle(r: float) -> float:
    """Return the area of a circle with radius r using math.pi."""
    return math.pi * (r ** 2)


def main():
    # Prompt the user and demonstrate the function.
    try:
        r_str = input("Enter the circle radius: ")
        r = float(r_str)
        area = areaOfCircle(r)
        print(f"Area of circle with radius {r}: {area:.4f}")
    except ValueError:
        print("Please enter a valid numeric radius.")


if __name__ == "__main__":
    main()