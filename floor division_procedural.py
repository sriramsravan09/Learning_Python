print("1st input")
a = input()
if int(a) < 0:
    print("na")
    exit()
else:
    print("1st num is " + a)
print("2nd input")
b = input()
if int(b) < 0:
    print("na")
    exit()
else:
    print("2nd num is " + b)

floor_div = int(a) // int(b)
print("results")
print(floor_div)