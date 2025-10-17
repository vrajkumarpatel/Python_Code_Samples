"""
Author: Vraj Patel, Manuel Sarmiento, Chyngyz Satarov
Date: 10/14/25
Purpose: This program lists an options to choose,
         and prints the chosen activity.
"""

option_list = {
1: "Go to cinema",
2: "Go to restaurant",
3: "Learn Language 'C'",
4: "Take a nap",
5: "Go to bed",
6: "Drive a car",
7: "Read a book",
8: "Drink a water",
0: "Exit the program"
}

    #Runs until user chooses to stop.
while True:

    #Print the header.
    print("\nPlease select the number of the option from below: ")
    print("-" * 50)

    #Print all the options.
    for number, option in option_list.items():
        print(f"{number}: {option}")

    #Get user input.
    user_input = int(input("\nEnter your choice: "))

    #1. Save the user input,
    #   and print it.
    #2. Check if the option is available.
    #3. If user inputs 0 quit the program.
    if user_input in option_list.keys():
        selected_option = option_list[user_input]
        print("You chose the option:", selected_option)
    else:
        print("\nThat option is not available, try again.")
    if user_input == 0:
        print("You chose to quit, thank you!")
        break