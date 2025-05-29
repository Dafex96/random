while True:
    print("\n--Calculator--")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit")

    opc = int(input("Enter an option: "))

    if opc == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        ans = num1 + num2
        print(f"The result of the addition is: {ans}")

    elif opc == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        ans = num1 - num2
        print(f"The result of the subtraction is: {ans}")

    elif opc == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        ans = num1 * num2
        print(f"The result of the multiplication is: {ans}")

    elif opc == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            ans = num1 / num2
            print(f"The result of the division is: {ans}")

    elif opc == 5:
        print("Quitting...")
        break

    else:
        print("Invalid option. Please try again.")