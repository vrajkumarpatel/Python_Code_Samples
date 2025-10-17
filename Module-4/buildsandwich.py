"""
Author: Dr. Antonio Tovar
Date: 10/14/25
Purpose: This program builds a sandwich with unique ingredients,
         it also overviews a while loop. 
"""

def buildsandwich(ingredients):
    if 'mayo' in ingredients:
        print("Sorry I don't like Mayo")
        return False
    else:
        return True

name = 'Vraj'
ingredients = ['ham', 'bread', 'tomatoes', 'mayo']

if buildsandwich(ingredients):
    print("Have a good meal!")
else:
    print("Sorry we run out of that.")

i = 1
while i <= 5:
    print("this is the value of i: ", i)
    i += 1