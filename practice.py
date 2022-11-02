def leapyear(y):
    z=int(input((y%4==0) and (y%100!=0) ) or (y%400==0))




leapyear(1996)



if year % 400 == 0:
    print("leap year1")
elif year % 4 == 0 and year % 100 !=0:
    print("leap year2")
    # maintain indentation and type how your output wants to look
else:
    print("not a leap year")
    exit()