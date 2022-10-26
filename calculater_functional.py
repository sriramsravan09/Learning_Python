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


# show the choice to user
print("Choose an option from the following :")
print("(1) Add (+)")
print("(2) Subtract (-)")
print("(3) Multiply (*)")
print("(4) Divide (/)")
print("(5) Find Remainder (%)")
print("(6) Find Quotient (//)")
print("(7) Find Square of a number (**)")



print("Calculator")


#print("enter the value for your numbers")
x=int(input("1st number:   "))
y = int(input("2nd number:   "))
if x<0 and y<0:
    print("please enter a positive number")
    exit()





option = input("Enter your option(1/2/3/4/5/6/7):  ")


if option == "1":
    add(x,y)


elif option == "2":
    sub(x,y)


elif option == "3":
    mul(x,y)


elif option == "4":
    div(x,y)

elif option == "5":
    expo(x,y)

elif option == "6":
    reminder(x,y)

elif option == "7":
    quotient(x,y)

else:
    exit()


