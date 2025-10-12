"""
Auther: Vraj Patel
Date: 09/23/2025

Purpose:

This program asks for name and age and prints the results to the screen


"""


# Auther: Vraj Patel
# Date: 09/23/2025



#The purpose of this program is to capture the user's name and age and display it back
#To the screen
#Grab the users name in a string

myname = input("Please enter your name: ")

age = input("Please enter your age: ")

print ("Hello" , myname, "you are ", age, "years old.")

print ("Hello {}, you are {} years old." .format(myname, age))

print (f"Hello {myname}, you are {age} years old.")


