# calculating leap year
# I want title as leap year
print("leap year")

# give year int input since it is a number
#

# logic to find leap year is first, number should be evenly divided by 4 and
# same time it should not evenly divided by 100
# then check if it is evenly dividing by 400

year = int(input("enter year:  "))
if year % 400 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 !=0:
    print("leap year")
    # maintain indentation and type how your output wants to look
else:
    print("not a leap year")
    exit()