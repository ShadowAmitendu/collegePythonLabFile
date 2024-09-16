# Write a python program to create a basic calculator.
def main():
    print("=====MENU=====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("=" * 15)
    print()
    choice_input()


def choice_input():
    print("=" * 15)
    choice = int(input("ENTER YOUR CHOICE:: "))
    a = float(input("ENTER FIRST NUMBER:: "))
    b = float(input("ENTER SECOND NUMBER:: "))
    calculate(choice, a, b)


def calculate(choice, a, b):
    if choice == 1:
        result = a + b
    elif choice == 2:
        result = a - b
    elif choice == 3:
        result = a * b
    elif choice == 4:
        result = a / b if b != 0 else "undefined (division by zero)"
    elif choice == 5:
        result = a // b if b != 0 else "undefined (division by zero)"
    else:
        result = "WRONG INPUT!"
    print(f"THE RESULT:: {result}")
    main()
    return


main()
