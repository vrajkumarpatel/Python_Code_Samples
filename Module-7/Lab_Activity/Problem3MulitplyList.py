# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 3: Multiply List
# Description: Write a Python function to multiply all the numbers in a list.
# Requirement: Use list [5, 2, 7, -1].


def multiply_list(nums: list[int]) -> int:
    """Return the product of all numbers in the list."""
    product = 1
    for x in nums:
        product *= x
    return product


def main():
    values = [5, 2, 7, -1]
    print(f"List: {values}")
    result = multiply_list(values)
    print(f"Product of list numbers: {result}")


if __name__ == "__main__":
    main()