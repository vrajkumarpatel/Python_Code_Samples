# Vrajkumar Patel
# 11/2/2025
# Problem 5 – Convert radians to degrees

import math

radians = float(input("Enter angle in radians: "))
degrees_manual = radians * (180 / math.pi)
degrees_math = math.degrees(radians)

print("Manual conversion:", degrees_manual)
print("Using math.degrees:", degrees_math)
