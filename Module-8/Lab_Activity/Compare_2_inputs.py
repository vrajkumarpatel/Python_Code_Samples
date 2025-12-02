# Vrajkumar Patel
# November 16, 2025
# Problem 1: Compares two user inputs for equality.

def compare_inputs():
    """Takes two inputs from a user and prints whether they are equal or not."""
    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")

    if input1 == input2:
        print(f"The values '{input1}' and '{input2}' are equal.")
    else:
        print(f"The values '{input1}' and '{input2}' are NOT equal.")

# Test the function
compare_inputs()