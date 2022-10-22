
#SO2NWS= sum of two numbers whole square
def SO2NWS(x,y):
    z=int(x)*int(x)+int(y)*int(y)+2*int(x)*int(y)
    print(z)

a=int(input("enter the value for first variable     "))
b=int(input("enter the value for second variable    "))

if a<=0 or b<=0:
    print("please give the value i.e >0")
    exit()
else:
    print("you entered good numbers")
print("results are")
SO2NWS(a,b)


