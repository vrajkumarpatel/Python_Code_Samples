# Vrajkumar Patel
# 11/2/2025
# Problem 6 – Compute factorial

import math

n = int(input("Enter a number: "))
factorial_manual = 1

for i in range(1, n + 1):
    factorial_manual *= i

print("Manual factorial:", factorial_manual)
print("Using math.factorial:", math.factorial(n))
