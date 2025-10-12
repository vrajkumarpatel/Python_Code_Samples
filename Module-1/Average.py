"""
Auther: Vraj Patel
Date: 09/23/2025

Purpose: This is a program to calculate average scores for all rounds

"""

#Number of rounds and Their scores
round1 = int(input("Enter score for round 1: ")) #Code to take input for round 1 and store value in round1
round2 = int(input("Enter score for round 2: ")) #Code to take input for round 2 and store value in round2
round3 = int(input("Enter score for round 3: ")) #Code to take input for round 3 and store value in round3

#Calculation of Average
average = (round1 + round2 + round3) / 3

#Print (Output)
print ("the average score is: ", average)
