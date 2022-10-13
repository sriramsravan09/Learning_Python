def expon(x, y):
    expon= int(p) ** int(q)
    print(expon)


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
expon = int(a) ** int(b)

print(expon)