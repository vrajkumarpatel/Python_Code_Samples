num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Type 'sum' to add or 'product' to multiply: ")

if choice == "sum":
    result = num1 + num2
    print("Result: " + str(result))
elif choice == "product":
    result = num1 * num2
    print("Result: " + str(result))
else:
    print("Invalid choice")