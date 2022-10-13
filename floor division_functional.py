def floor_div(x, y):
    floor_div = int(p) // int(q)
    print(floor_div)


print("first input")
a = input()
if int(a) < 0:
    print("not valid")
    exit()
else:
    print("first number is " + a)
print("second input")
b = input()
if int(b) < 0:
    print("not valid ")
    exit()
else:
    print("second number is " + b)
    print("result")
floor_div = int(a) // int(b)

print(floor_div)