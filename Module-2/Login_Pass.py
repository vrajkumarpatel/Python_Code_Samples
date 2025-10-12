username = input("Enter username: ")
password = input("Enter password: ")
# pretend we have saved values
saved_username = "admin"
saved_password = "1234"
if username == saved_username and password == saved_password:
    print("Login successful")
else:
    print("Login failed")
