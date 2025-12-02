# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Chapter 2 Module: bypass_lock.py
# Action: Bypass the lock manually (a difficult electronic puzzle) to access the main research lab.
# Outcome: Success opens the corridor; Failure results in a lockout.

import time
import random


def bypass_lock_puzzle(player_intelligence: int) -> str:
    """Simulates a difficult electronic puzzle to bypass a locked door."""
    difficulty_rating = 3
    moves_made = 0
    max_attempts = 5

    print("\n--- Electronic Bypass Puzzle Initiated ---")

    while moves_made < difficulty_rating and max_attempts > 0:
        print(
            f"Attempts Remaining: {max_attempts}. Frequencies Matched: {moves_made}/{difficulty_rating}"
        )

        # Chance of success improves with player_intelligence
        chance_of_correct_move = 30 + (player_intelligence * 2)

        choice = input("Adjust Emitter (A, B, or C) or Give Up (G): ").upper()

        if choice == "G":
            return "GIVE_UP"

        if random.randint(1, 100) <= chance_of_correct_move:
            moves_made += 1
            print(f">> SUCCESS! Emitter {choice} aligned.")
        else:
            max_attempts -= 1
            print(">> ERROR! The frequency jumps.")
            if max_attempts == 0:
                print("\nThe system sealed the door.")
                return "LOCKOUT"

        time.sleep(0.5)

    if moves_made == difficulty_rating:
        print("\n**>> LOCK BYPASSED! <<** Proceed to Chapter 3.")
        return "SUCCESS"


def main():
    try:
        intel = int(input("Enter your intelligence (0-100): "))
    except ValueError:
        print("Please enter a valid integer for intelligence.")
        return

    result = bypass_lock_puzzle(intel)
    print(f"Outcome: {result}")


if __name__ == "__main__":
    main()