# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Chapter 3 Module: interrogate_researcher.py
# Action: Question the Lead Researcher to find a subtle clue.
# Outcome: Find a subtle clue about the mind control technology (Success) or gain nothing (Failure).

import random


def interrogate_researcher() -> str:
    """Handles dialogue choices and outcome when questioning the Lead Researcher."""
    clue_found = False
    max_questions = 3

    print("\n--- Interrogating Lead Researcher ---")
    print("Researcher: 'It was a terrible accident. The Core Regulator is gone!'")

    while max_questions > 0 and not clue_found:
        print(f"\nQuestions Remaining: {max_questions}")
        choice = input(
            "1: Focus on the time. 2: Ask about test subjects. 3: Demand logs. Enter choice (1-3): "
        )

        if choice == "2":
            # This is the 'correct' line of questioning for the clue
            print(
                "Player: 'Did any of the test subjects seem unstable? Particularly Subject Gamma-7.'"
            )
            print(
                "Researcher: 'No, they were... dormant. That's the point of the **Synaptic Override Device**, isn't it?'"
            )
            clue_found = True
        elif choice == "1":
            print(
                "Player: 'The security log shows a time discrepancy.' Researcher: (Sweats) 'I must have misremembered.'"
            )
        elif choice == "3":
            print(
                "Player: 'Show me the last hour of control logs.' Researcher: 'I can't! They're corrupted!'"
            )

        max_questions -= 1

    if clue_found:
        print("\n**>> CLUE OBTAINED! <<** You learned about the Synaptic Override Device.")
        return "CLUE_FOUND"  # Success
    elif max_questions == 0:
        print(
            "\nTime is running out. The Researcher is too panicked to give you anything useful."
        )
        return "TIME_WASTED"  # Failure


def main():
    outcome = interrogate_researcher()
    print(f"Outcome: {outcome}")


if __name__ == "__main__":
    main()