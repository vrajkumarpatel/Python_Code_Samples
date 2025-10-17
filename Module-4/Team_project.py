
def run_menu():
    """
    Author: Vreaj Patel, Manuel Sarmiento, Chyngyz Satarov 
    Date: 10/14/2025
    Purpose: Displays a numbered menu and allows the user to select an option
    or exit the program. 
    """
    # The menu options
    options = {
        '1': "Go Home",
        '2': "Want to go Home",
        '3': "Do you want to go home?",
        '4': "Dont go Home",
        '5': "I am from Home",
        '6': "Home is from me.....",
        '7': "Me is from Home"
    }

    # Loop 
    while True:
        # menu header
        print("-" * 35)
        print("Please choose your option from the list below:")
        print("-" * 35)

        # Print the numbered options
        for key, value in options.items():
            print(f"{key}. {value}")

        # Exit option 
        print("0. Exit Program and go Home")
        print("-" * 35)

        # user's choice
        user_choice = input("Enter your choice (0-7): ").strip()

        # if/elif/else 
        if user_choice == '0':
            print("\n>> Exit successful. You chose: 0. Program terminated and now go Home!......")
            # Break the while loop to exit the program
            break
        elif user_choice in options:
            # valid choices (1 through 7)
            message = options[user_choice]
            print(f"\n✅ SUCCESS! You selected option now go Home! {user_choice}: '{message}'.")
        else:
            # Handle invalid input  
            print(f"\n❌ Invalid choice: {user_choice}. Please enter a number between 0 and 7 or go Home!")
        
        # Add a blank line 
        print("\n")


if __name__ == "__main__":
    run_menu()
