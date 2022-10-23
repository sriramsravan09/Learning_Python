# calculating leap year
# I want title as leap year
print("leap year")

# give year int input since it is a number


# logic to find leap year is first, number should be evenly divided by 4 and
# same time it should not evenly divided by 100
# then check if it is evenly dividing by 400

year = int(input("enter year:  "))
if year<=0:
    print ("you entered a in valid number")
elif year%4==0 and year%100!=0:
    print("1st condition satisfied , it is a leap year")
elif year%400==0:
    print("all three conditions satisfied and it is a leap year")
else:
    print("not a leap year")