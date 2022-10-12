# get the first number
# print(*enter first input*)
def add(a, b):
    sum = a + b
    return sum
# Taking input
num1 = int(input("first number: "))
num2 = int(input("second number: "))
# call function
sum = add(num1, num2)
# result
print("Sum of two numbers is: ", sum)