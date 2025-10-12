"""
Auther: Vraj Patel
Date: 09/23/2025

Purpose: This is a username login system

"""
# Ask the user to input their username
username = input("Login: >> ")

# two valid usernames
user1 = "Jack"
user2 = "Jill"

# Check if the entered username matches the first user
if username == user1:
    print("Access granted")

# If not Jack, check if the username matches the second user
elif username == user2:
    print("Welcome to the system")

# If doesnt match deny access
else:
    print("Access denied")
