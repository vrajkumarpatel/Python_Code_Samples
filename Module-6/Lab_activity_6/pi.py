# Vrajkumar Patel
# 11/2/2025
# Problem 4 – Approximate pi and compare to math.pi

import math

# Leibniz formula for pi
iterations = 100000
approx_pi = 0
for k in range(iterations):
    approx_pi += ((-1) ** k) / (2 * k + 1)
approx_pi *= 4

print("Approximated pi:", approx_pi)
print("math.pi:", math.pi)
