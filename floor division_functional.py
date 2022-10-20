def flo_div(a,b):
    flo_div = int(a) // int(b)
    print("results are")


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
flo_div = int(a) // int(b)

print(flo_div)