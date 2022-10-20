def add(x,y):
    add=int(x)+int(y)
    print("results are")
    print(add)


a=int(input("1stnumber"))
if a<0:
    print("na")
else:
    print("you entered",  a)

b=int(input("2ndnumber"))
if b<0:
    print("na")
else:
    print("you also entered",  b)


add(a,b)
print(add)