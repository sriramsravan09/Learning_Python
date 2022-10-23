def add(x,y):
    add=int(x)+int(y)
    print("results are",   add)


def sub(x,y):
    sub=int(x)+int(y)
    print("results are",   sub)



def mul(x,y):
    mul=int(x)*int(y)
    print("results are",  mul)



def div(x,y):
    div=int(x)/int(y)
    print("results are",   div)


def expo(x,y):
    expo=int(x)**int(y)
    print("results are",    expo)


def reminder(x,y):
    reminder=int(x)%int(y)
    print("results are",    reminder)



def quotient(x,y):
    quotient=int(x)//int(y)
    print("results are",    quotient)





print("calculater")


print("enter the value for your numbers")
x=int(input("1st number   "))
y = int(input("2nd number   "))
if x>=0 and y>0:
    print("you entered valid numbers")
else:
    print("NA")
    exit()

print('''
        + addition
        - sub
        * mul
        / div
        ** expo
        % reminder
        // quotient
        ''')


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


