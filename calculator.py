def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    return x / y


def calculator():
    print("Welcome to the calculator!")
    print("Select an operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter a choice(1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter a first number: "))
            num2 = float(input("Enter a second number: "))

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Would you like to do another calculation? (y/n): ")
            if next_calculation.lower() != "y":
                break
        else:
            print("Please enter a valid choice")


if __name__ == "__main__":
    calculator()
