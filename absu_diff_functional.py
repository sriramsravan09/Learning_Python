def abb_diff(x, y):
    abb_diff = int(x) - int(y)
    if abb_diff < 0:
        print(-abb_diff)
    else:
        print(abb_diff)
x=int(input("1st num     "))
y=int(input("2nd num    "))
print("results are")
abb_diff(x,y)





