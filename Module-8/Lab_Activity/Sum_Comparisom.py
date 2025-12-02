# Vrajkumar Patel
# November 16, 2025
# Problem 2: Takes two inputs, sums them, and compares the sum to 10.

def sum_comparison():
    """Takes two numerical inputs and prints whether their sum is > 10, < 10, or = 10."""
    try:
        # Get numerical inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        total_sum = num1 + num2
        
        if total_sum > 10:
            print(f"The sum ({total_sum}) is greater than 10.")
        elif total_sum < 10:
            print(f"The sum ({total_sum}) is less than 10.")
        else:
            print(f"The sum ({total_sum}) is equal to 10.")
            
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Test the function
sum_comparison()