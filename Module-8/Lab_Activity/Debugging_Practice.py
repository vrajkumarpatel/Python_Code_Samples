"""# The original code with a logical error (BUG)
def check_range_buggy(number):

    Intended to check if a number is between 10 and 20 (inclusive), 
    but contains a common logical error.
    
    # BUG: This checks (10 <= number) AND (20). (20) evaluates as True, 
    # so the condition is 10 <= number. It ignores the upper bound check.
    if 10 <= number and 20: 
        print(f"BUGGY: {number} is in the range.")
    else:
        print(f"BUGGY: {number} is NOT in the range.")

print("--- Problem 7: Debugging Practice (Common Boolean Error) ---")
check_range_buggy(5)   # Expected: NOT in range. Actual: Correct.
check_range_buggy(15)  # Expected: in range. Actual: Correct.
check_range_buggy(25)  # Expected: NOT in range. Actual: **INCORRECTLY reports 'in the range.'**
"""

# Vrajkumar Patel
# November 16, 2025
# Problem 7: Debugging Practice (Fixed Code)

def check_range_fixed(number):
    """
    FIXED: Correctly checks if a number is between 10 and 20 (inclusive).
    Uses the correct boolean logic: (10 <= number) AND (number <= 20).
    """
    # Python allows for simple chained comparison: 
    if 10 <= number <= 20: 
        print(f"FIXED: {number} is in the range.")
    else:
        print(f"FIXED: {number} is NOT in the range.")

# Test the fixed function
check_range_fixed(5)
check_range_fixed(15)
check_range_fixed(25)
print("-" * 20)