# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 4: Unique Elements
# Description: Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list.
# Requirement: Use list [1, 3, 3, 3, 6, 2, 3, 5] and use the append function.


def unique_list(nums: list[int]) -> list[int]:
    """Return a new list containing unique elements from nums, preserving order."""
    uniques: list[int] = []
    for x in nums:
        if x not in uniques:
            uniques.append(x)  # requirement: use append
    return uniques


def main():
    source = [1, 3, 3, 3, 6, 2, 3, 5]
    print(f"Original list: {source}")
    uniques = unique_list(source)
    print(f"Unique elements: {uniques}")


if __name__ == "__main__":
    main()