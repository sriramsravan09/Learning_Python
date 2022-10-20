# program for a calculater
# choose what operators you want to include
# write a print statement with tripple ' so that you can display the operators.
# writing strings in multiple lines should be in tripple quotes


print("calculator")
print(
     ''' + add
      - Sub
      * Mul
      / Div
      * Expo
      % module
      // quotient''')

# let user choose the operater symbol which mentioned above
operator = input("enter the symbol")
# give the values for x and y
x = int(input("1st number"))
if x>=0:
    print("keep going")
else:
    print("stop")
y = int(input("2nd number"))
if y>0:
    print("keep going")
else:
    print("stop")
# perform operation based on user choice
if operator == "+":
 print("results are")
 print(x+y)
elif operator == "-":
    print("results are")
    print(x-y)
elif operator == "*":
    print("results are")
    print(x*y)
elif operator == "/":
    print("results are")
    print(x/y)
elif operator == "%":
    print("results are")
    print(x%y)
elif operator == "**":
    print("results are")
    print (x**y)
elif operator == "//":
    print("results are")
    print(x//y)
else:
    print("check the symbol")
