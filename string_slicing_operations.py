#Program should accept a string value while running
x=input("what is the string")

#find out the slice of that string after removing first and last character
y=len(x)
x1=x[1:-1]
print(x1)

#.Find out the slice of the string after removing the first 2 characters


x2=x[2:]
print(x2)
#Find out the slice of the string after removing the last 2 characters
x3=x[:-2]
print(x3)

#Slice the string in the middle and display both strings.
x4=x[:int(len(x)//2)]
x5=x[int(len(x)//2):]
print(x4,x5)