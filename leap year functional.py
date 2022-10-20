def leapyear(x):
    return (x % 4 == 0 and x % 100 != float) or x % 400 == 0
    print("leapyear")

x = int(input("year:  "))
if x <= 0:
    print("year cannot be zero or negative")
elif (leapyear(x)):
 print("hurry it is a leap year")
else:
 print("oops it is a not a leap year")

