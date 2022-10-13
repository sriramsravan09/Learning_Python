# get the first number
# print(*enter first input*)
def sub(x, y):
    sub = int(p) - int(q)
    print(sub)

x = input("enter first input")
print("first value is" + x)
print("enter second input")
y = input("enter second input")
print("second value is" + y)
# sub the numbers and store the results
print("results")
z = (int(x) - int(y))
if z < 0:
    print(-z)
else:
    print(z)