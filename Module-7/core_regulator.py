# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Title: The Core Regulator — Terminal Adventure Driver
# Description: Playable terminal game that orchestrates Chapters 1–5 using the
# provided modules. Navigate choices, make skill checks, and reach one of
# several endings.

import sys
from typing import Dict

# Import chapter modules (placed at project root)
from hack_terminal import hack_terminal
from bypass_lock import bypass_lock_puzzle
from interrogate_researcher import interrogate_researcher
from analyze_device import analyze_control_device
from combat_sequence import fight_mastermind


def hr():
    print("\n" + "=" * 70)


def ask_choice(prompt: str, options: Dict[str, str]) -> str:
    """Prompt for a choice until a valid key in options is given."""
    while True:
        print(prompt)
        for key, desc in options.items():
            print(f"  {key}: {desc}")
        choice = input("Select: ").strip().upper()
        if choice in options:
            return choice
        print("Invalid selection. Please try again.")


def ask_int(prompt: str, min_v: int = 0, max_v: int = 100) -> int:
    """Prompt for an integer within [min_v, max_v]."""
    while True:
        try:
            v = int(input(prompt).strip())
            if min_v <= v <= max_v:
                return v
            print(f"Please enter a value between {min_v} and {max_v}.")
        except ValueError:
            print("Please enter a valid integer.")


def chapter1(state: Dict) -> str:
    hr()
    print("Chapter 1: The Docking Bay Infiltration")
    print("\"The cold void of space was a stark contrast to the buzzing neon of the docking bay. Your mission timer starts now.\"")
    while True:
        hr()
        choice = ask_choice(
            "Actions:",
            {
                "T": "Talk to dock workers (gain stealth knowledge)",
                "H": "Hack a terminal (risk alert)",
                "S": "Search for a maintenance shaft (stealthy access)",
                "L": "Leave the station (Game Over)",
            },
        )

        if choice == "T":
            print("You learn patrol routes and shift changes. Stealth increased.")
            state["stealth_knowledge"] = True
        elif choice == "H":
            skill = ask_int("Enter your hacking skill (0-100): ")
            outcome = hack_terminal(skill)
            if outcome == "PASS_OBTAINED":
                state["has_access"] = True
                state["access_path"] = "pass"
                print("You slip into the restricted levels using the temporary pass.")
                return "CH2"
            elif outcome == "ALERT_RAISED":
                state["alert_raised"] = True
                print("Security is now on alert. You'll need a stealthier route.")
            else:
                print("Terminal locked you out. Try another method.")
        elif choice == "S":
            print("You pry open a maintenance panel and crawl through the dark shafts.")
            state["has_access"] = True
            state["access_path"] = "shaft"
            return "CH2"
        elif choice == "L":
            print("You abandon the mission. Corporate Security will handle the fallout.")
            return "GAME_OVER"


def chapter2(state: Dict) -> str:
    hr()
    print("Chapter 2: The Restricted Zone")
    print("\"The research deck was eerily silent, the only sound the faint, rhythmic whirring from within the subject cells.\"")

    while True:
        hr()
        choice = ask_choice(
            "Actions:",
            {
                "F": "Search the subject (find a keycard)",
                "W": "Wake the subject (danger)",
                "B": "Bypass the lock manually (puzzle)",
                "D": "Go back to the docking bay",
            },
        )

        if choice == "F":
            print("You find a keycard tucked under the subject's sleeve.")
            state["has_keycard"] = True
            print("The corridor door slides open.")
            return "CH3"
        elif choice == "W":
            print("You jolt the subject awake. They thrash wildly!")
            # Simple danger outcome: coin flip
            from random import randint

            if randint(1, 100) > 55:
                print("You subdue the subject and grab the keycard.")
                state["has_keycard"] = True
                return "CH3"
            else:
                print("You are overwhelmed. The mission ends here.")
                return "GAME_OVER"
        elif choice == "B":
            intel = ask_int("Enter your intelligence (0-100): ")
            result = bypass_lock_puzzle(intel)
            if result == "SUCCESS":
                print("You save crucial time and open the corridor.")
                return "CH3"
            elif result == "LOCKOUT":
                print("Lockout engaged. Without a keycard, you're stuck.")
                if state.get("has_keycard"):
                    print("Keycard overrides the lockout. Proceed.")
                    return "CH3"
            elif result == "GIVE_UP":
                print("You step away from the lock. Maybe another approach.")
        elif choice == "D":
            print("You retrace your steps to the docking bay.")
            return "CH1"


def chapter3(state: Dict) -> str:
    hr()
    print("Chapter 3: The Lab Encounter")
    print("\"The main lab was a mess—broken equipment, spilled chemicals, and a single, frantic researcher trying to contain the damage.\"")

    while True:
        hr()
        choice = ask_choice(
            "Actions:",
            {
                "Q": "Question the Researcher (module)",
                "S": "Search the lab quietly (hidden log)",
                "A": "Accuse the Researcher (trigger lockdown)",
                "R": "Return to restricted corridor",
            },
        )

        if choice == "Q":
            result = interrogate_researcher()
            if result == "CLUE_FOUND":
                state["clue_found"] = True
                print("A clue points to Subject Gamma-7. The cell is empty...")
                return "CH4"
            else:
                print("You learned little. The lab remains uneasy.")
        elif choice == "S":
            print("You uncover a hidden log entry: Gamma-7 was moved. The cell is empty.")
            state["clue_found"] = True
            return "CH4"
        elif choice == "A":
            print("The Researcher slams the lockdown switch. Sirens blare; the cells seal.")
            state["lockdown"] = True
            return "CH4"
        elif choice == "R":
            print("You leave the lab and return to the corridor.")
            return "CH2"


def chapter4(state: Dict) -> str:
    hr()
    print("Chapter 4: The Traced Subject")
    print("\"The log pointed to Test Subject Gamma-7... The cell was empty. A faint trail of oil led into the dark utility shafts.\"")
    state["device_found"] = True

    while True:
        hr()
        choice = ask_choice(
            "Actions:",
            {
                "A": "Analyze the discarded control device (module)",
                "F": "Follow the oil trail deeper (toward escape pods)",
                "S": "Send a fake distress signal (buy time, risky)",
                "B": "Go back to the lab",
            },
        )

        if choice == "A":
            tech = ask_int("Enter your tech expertise (0-100): ")
            outcome = analyze_control_device(tech)
            if outcome == "MASTERMIND_REVEALED":
                state["mastermind_known"] = True
                state["has_device_usable"] = True
                print("You pocket the device—battery seems good enough for one critical use.")
            else:
                state["has_device_usable"] = False
                print("Battery is dead. You keep the shell as evidence.")
        elif choice == "F":
            print("You move through tight passages to the escape pod bay.")
            return "CH5"
        elif choice == "S":
            from random import randint
            print("You broadcast a fabricated emergency. Will anyone fall for it?")
            if randint(1, 100) <= 40:
                print("The ruse works. Patrols split up, buying you time.")
                state["bought_time"] = True
            else:
                print("Security triangulates your position. You barely slip away.")
                state["alert_raised"] = True
        elif choice == "B":
            print("You return to the lab and find the Researcher dead. The trail calls you onward.")
            return "GAME_OVER"


def chapter5(state: Dict) -> str:
    hr()
    print("Chapter 5: Final Confrontation")
    print("\"The escape pod bay was small—Gamma-7 clutching the Core Regulator, and the true Mastermind.\"")

    while True:
        hr()
        choice = ask_choice(
            "Actions:",
            {
                "F": "Fight the Mastermind (module)",
                "U": "Use the control device to free Gamma-7 (if usable)",
                "S": "Surrender to the Mastermind (Game Over)",
                "E": "Attempt to escape without the Regulator (Game Over)",
            },
        )

        if choice == "F":
            combat = ask_int("Enter your combat skill (0-100): ")
            result = fight_mastermind(combat, bool(state.get("has_device_usable", False)))
            return result
        elif choice == "U":
            if not state.get("has_device_usable", False):
                print("The device is dead. You must try another way.")
                continue
            # Reuse fight module prompt for U vs C while ensuring device flag is True
            combat = ask_int("Enter your combat skill (0-100): ")
            result = fight_mastermind(combat, True)
            return result
        elif choice == "S":
            print("You lower your weapon and surrender. The Mastermind smiles.")
            return "SURRENDER_ENDING"
        elif choice == "E":
            print("You sprint to an empty pod. Security swarms in. Without the Regulator, you're detained.")
            return "CAPTURED_ENDING"


def epilog(outcome: str) -> None:
    hr()
    print("Mission Outcome:")
    if outcome == "WIN_ENDING":
        print(
            "You escape Elysium with the Core Regulator. The corporation hails you as a hero—until the internal audit begins."
        )
    elif outcome == "CAPTURED_ENDING":
        print(
            "Corporate Security arrests you on the spot. The Mastermind vanishes into the black.")
    elif outcome == "SURRENDER_ENDING":
        print("The Mastermind departs in a pod, leaving you to face the consequences.")
    else:
        print("The trail goes cold. Elysium returns to silence.")
    hr()


def main():
    state: Dict = {
        "stealth_knowledge": False,
        "has_access": False,
        "alert_raised": False,
    }

    current = "CH1"
    while True:
        if current == "CH1":
            current = chapter1(state)
        elif current == "CH2":
            current = chapter2(state)
        elif current == "CH3":
            current = chapter3(state)
        elif current == "CH4":
            current = chapter4(state)
        elif current == "CH5":
            outcome = chapter5(state)
            epilog(outcome)
            break
        elif current == "GAME_OVER":
            epilog("SURRENDER_ENDING")
            break
        else:
            print("Unknown chapter. Exiting.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting The Core Regulator. Goodbye.")
        sys.exit(0)