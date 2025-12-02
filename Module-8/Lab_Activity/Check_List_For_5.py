# Vrajkumar Patel
# November 16, 2025
# Problem 3: Checks if the value 5 is in a given list.

def check_for_five(input_list):
    """Takes a list and prints if the value 5 is in that list."""
    # The 'in' operator returns a boolean (True/False)
    if 5 in input_list:
        print(f"The value 5 IS in the list: {input_list}")
    else:
        print(f"The value 5 is NOT in the list: {input_list}")

# Test the function
test_list_1 = [1, 2, 5, 8, 9]
test_list_2 = [10, 20, 30]

check_for_five(test_list_1)
check_for_five(test_list_2)