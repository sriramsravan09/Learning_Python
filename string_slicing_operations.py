#Program should accept a string value while running
x=input("Enter a string value    ")
print(x)
print("You entered:",x)

#find out the slice of that string after removing first and last character
y=len(x)
x1=x[1:-1]
print("Slice of", x, "after removing first and last character is",x1)

#.Find out the slice of the string after removing the first 2 characters


x2=x[2:]
print("Slice of", x,"after removing the first 2 characters is",x2)

#Find out the slice of the string after removing the last 2 characters

x3=x[:-2]
print("Slice of the",x, "after removing the last 2 characters is",x3)

#Slice the string in the middle and display both strings.
print("Mid index is", len(x) // 2)
x4=x[:int(len(x)//2)]
x5=x[int(len(x)//2):]
print("First half slice of",x, "is",x4)
print("Second half slice of",x, "is",x5)