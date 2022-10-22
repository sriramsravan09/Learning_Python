def leap_year(y):
    leap_year = int(input(((y % 4 == 0)) and (y % 100 !=0)) or (y % 400 == 0))


# it is boolen :-    true = leap year : false = not a leap year
print("enter the year")
y=int(input("year"))
if y>0:
    print("TRUE = LEAPYEAR........ FALSE = NOT A LEAP YEAR")
    print("you entered a valid number")
    print("results are")
    leap_year(y)
else:
 print("na")











