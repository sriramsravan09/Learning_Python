def add(x,y):
    add=int(x)+int(y)
    print("results are")
    print(add)

def sub(x,y):
    sub=int(x)+int(y)
    print("results are")
    print(sub)


def mul(x,y):
    mul=int(x)*int(y)
    print("results are")
    print(mul)


def div(x,y):
    div=int(x)/int(y)
    print("results are")
    print(div)

def expo(x,y):
    expo=int(x)**int(y)
    print("results are")
    print(expo)


def reminder(x,y):
    reminder=int(x)%int(y)
    print("results are")
    print(reminder)


def quotient(x,y):
    quotient=int(x)//int(y)
    print("results are")
    print(quotient)




print("calculater")

print('''
        + addition
        - sub
        * mul
        / div
        ** expo
        % reminder
        // quotient
        ''')

print("enter the value for your number")
x=int(input("1st value is   "))
y=int(input("2nd value is  "))

print("seclect the operator")

operator=input("symbol   ")


if operator=="+":
    add(x,y)


elif operator=="-":
    sub(x,y)


elif operator=="*":
    mul(x,y)


elif operator=="/":
    div(x,y)

elif operator=="**":
    expo(x,y)

elif operator=="%":
    reminder(x,y)

elif operator=="//":
    quotient(x,y)

else:
    print("invalid symbol")
    exit()


