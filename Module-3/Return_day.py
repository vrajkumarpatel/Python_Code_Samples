# Name: Vrajkumar Patel
# Date: 2025-10-12
# Module 3 Lab Activity – Programming Solutions

start_day = int(input("Enter the starting day number (0=Sun, 6=Sat): "))
length_of_stay = int(input("Enter the length of your stay (in nights): "))
return_day = (start_day + length_of_stay) % 7
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"You will return home on day {return_day}, which is {days_of_week[return_day]}")