# calculating leap year
# I want title as leap year
print("leap year")

# give year int input since it is a number
year = int(input("enter year:  "))

# logic to find leap year is first, number should be evenly divided by 4 and
# same time it should evenly divided by 100 and quotient should not be a float
# then check if it is evenly dividing by 400

if year % 400 == 0:
    print("yes1")
elif year % 100 != 0:
    print("yes2")
elif (year % 4 == 0 ):
    print("yes3")

    # maintain indentation and type how your output wants to look
else:
    print("no")
