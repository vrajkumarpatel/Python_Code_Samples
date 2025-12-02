# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Chapter 4 Module: analyze_device.py
# Action: Analyze the discarded control device found in the ventilation shafts.
# Outcome: Player learns the true identity of the mastermind (Success) or the device fails (Failure).

import random


def analyze_control_device(player_tech_expertise: int) -> str:
    """Simulates the player analyzing the control device to uncover the mastermind's identity."""
    data_integrity_threshold = 70
    base_chance = player_tech_expertise + random.randint(10, 30)

    print("\n--- Analyzing Discarded Control Device ---")

    if base_chance >= data_integrity_threshold:
        print(
            ">> DATA EXTRACTED << You cross-reference the data and **uncover the Mastermind's identity**! Proceed to Chapter 5 with vital knowledge."
        )
        return "MASTERMIND_REVEALED"  # Success
    else:
        print(
            ">> DEVICE FAILED << The device's battery died. The identity remains a mystery. Proceed to Chapter 5 without proof."
        )
        return "IDENTITY_UNKNOWN"  # Failure


def main():
    try:
        expertise = int(input("Enter your tech expertise (0-100): "))
    except ValueError:
        print("Please enter a valid integer for tech expertise.")
        return

    outcome = analyze_control_device(expertise)
    print(f"Outcome: {outcome}")


if __name__ == "__main__":
    main()