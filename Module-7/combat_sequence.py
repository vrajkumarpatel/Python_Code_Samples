# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Chapter 5 Module: combat_sequence.py
# Action: Fight the Mastermind (The final confrontation).
# Outcome: Win (Successful Escape Ending) or Loss (Captured/Mastermind Escapes Ending).

import random


def fight_mastermind(player_combat_skill: int, has_control_device: bool) -> str:
    """Simulates the final confrontation using a skill check or a strategic option."""
    mastermind_combat_difficulty = 75
    player_score = player_combat_skill + random.randint(1, 20)

    print("\n--- Confrontation: Mastermind vs. Corporate Investigator ---")

    if has_control_device and input(
        "Use the control device to free Gamma-7 (U) or Initiate direct combat (C)? "
    ).upper() == "U":
        print("You override the mind-control. Gamma-7 attacks the Mastermind!")
        print("**>> STRATEGIC WIN! <<** You secure the Regulator and escape amidst the chaos.")
        return "WIN_ENDING"  # Alternate Success ending

    # If direct combat is chosen or device is not available
    if player_score >= mastermind_combat_difficulty:
        print("\n**>> SUCCESS! <<** You neutralize the Mastermind and secure the **Core Regulator**.")
        return "WIN_ENDING"
    else:
        if player_score >= mastermind_combat_difficulty - 15:
            print("\nThe Mastermind overpowers you and frames you for the crime.")
            return "CAPTURED_ENDING"  # Game Over
        else:
            print("\nThe Mastermind escapes and you are captured.")
            return "SURRENDER_ENDING"  # Game Over


def main():
    try:
        combat = int(input("Enter your combat skill (0-100): "))
    except ValueError:
        print("Please enter a valid integer for combat skill.")
        return

    have_device_input = input("Do you have the control device from Chapter 4? (y/n): ").strip().lower()
    has_device = have_device_input.startswith("y")

    result = fight_mastermind(combat, has_device)
    print(f"Outcome: {result}")


if __name__ == "__main__":
    main()