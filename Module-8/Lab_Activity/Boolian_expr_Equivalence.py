# Vrajkumar Patel
# November 16, 2025
# Problem 6: Demonstrates the equivalence of three boolean expressions.

# Set sample values for testing the equivalence
sword_charge = 0.95
shield_energy = 120

print(f"--- Testing Equivalent Conditions ---")
print(f"Sword Charge: {sword_charge}, Shield Energy: {shield_energy}\n")

# Version 1 (Original, focusing on the attack FAILURE condition using 'not') [cite: 14]
print("Version 1 (Original Condition)")
if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
print("-" * 15)

# Version 2 (Using De Morgan's Law) [cite: 15, 16]
# NOT (A AND B) is equivalent to (NOT A) OR (NOT B)
print("Version 2 (De Morgan's Law: not (A and B) -> (not A) or (not B))")
if (sword_charge < 0.90) or (shield_energy < 100):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
print("-" * 15)

# Version 3 (Swapping 'then'/'else' to remove 'not') [cite: 17, 19]
print("Version 3 (Simplified by swapping 'then'/'else')")
if (sword_charge >= 0.90) and (shield_energy >= 100):
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
else:
    print("Your attack has no effect, the dragon fries you to a crisp!")
print("-" * 15)