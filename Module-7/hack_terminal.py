# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Chapter 1 Module: hack_terminal.py
# Action: Hack a terminal to obtain a temporary security pass.
# Outcome: Success grants access; Failure may raise a security alert.

import random


def hack_terminal(player_hacking_skill: int) -> str:
    """Simulates the player attempting to hack a restricted terminal."""
    system_difficulty = 60
    base_success_chance = player_hacking_skill - (system_difficulty * 0.5)
    roll = random.randint(1, 100)

    print("\n--- Initiating Terminal Hack ---")

    if roll + base_success_chance >= 75:
        print(">> ACCESS GRANTED << You gain a temporary security pass.")
        return "PASS_OBTAINED"  # Success: Proceed to Chapter 2
    else:
        if roll < 30:
            print(
                ">> ACCESS DENIED - ALERT << Security alert raised. Try the maintenance shaft."
            )
            return "ALERT_RAISED"  # Failure with complication
        else:
            print(">> ACCESS DENIED << System locked you out.")
            return "FAILED"  # Failure: Player must choose another action


def main():
    try:
        skill = int(input("Enter your hacking skill (0-100): "))
    except ValueError:
        print("Please enter a valid integer for hacking skill.")
        return

    outcome = hack_terminal(skill)
    print(f"Outcome: {outcome}")


if __name__ == "__main__":
    main()