A=int(input("Enter a number"))
print(" You entered  '",A,"'")
B=int(input("How many odd numbers you want to print"))
print("printing", B, "odd numbers after", A)
C=2*B-1
for i in range(A,C):
 if i % 2 != 0:
  print(i)







