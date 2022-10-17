# Program make a simple calculator

# 1 Adds two numbers
def add(p, q):
    return p + q



# 2 Sub two numbers
def subtract(p, q):
    return p - q


# 3 Multi two numbers
def multiply(p, q):
    return p * q


# 4 Divides two numbers
def divide(p, q):
    return P / q

# 5 Remainder
def remainder(p, q):
    return p % q


# 6 Quotient(//)
def quotient(p, q):
    return p // q

# 7 Expo(**)
def expo(p,q):
    return p ** q


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Quotient")
print("7.Expo")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        if choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", remainder(num1, num2))

        elif choice == '6':
            print(num1, "//", num2, "=", quotient(num1, num2))

        elif choice == '7':
            print(num1, "**", num2, "=", expo(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break