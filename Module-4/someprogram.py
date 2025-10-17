# Import the datetime module to work with the current year
import datetime

# Function to calculate the year of birth based on the user's age
def calculate_birth_year(age):
    # Get the current year using the datetime module
    current_year = datetime.datetime.now().year
    # Subtract the user's age from the current year to find the birth year
    birth_year = current_year - age
    return birth_year

# Function to calculate BMI based on the user's weight (in kilograms) and height (in meters)
def calculate_bmi(weight, height):
    # BMI formula: BMI = weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    return bmi

# Main function to interact with the user
def main():
    # Ask the user for their age
    age = int(input("Please enter your age: "))
    
    # Calculate the year the user was born
    birth_year = calculate_birth_year(age)
    # Display the birth year to the user
    print(f"You were born in the year: {birth_year}")
    
    # Ask the user for their weight in kilograms
    weight = float(input("Please enter your weight in kilograms: "))
    
    # Ask the user for their height in meters
    height = float(input("Please enter your height in meters: "))
    
    # Calculate the user's BMI using the weight and height they provided
    bmi = calculate_bmi(weight, height)
    # Display the BMI to the user, rounding it to 2 decimal places for readability
    print(f"Your BMI is: {bmi:.2f}")

# Entry point of the program
if __name__ == "__main__":
    # Run the main function to start the program
    main()
