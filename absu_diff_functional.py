def abb_diff(x, y):
    abb_diff = int(x) - int(y)
    print(abb_diff)


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
abb_diff = int(a) - int(b)
if abb_diff < 0:
    print(-abb_diff)
else:
    print(abb_diff)


