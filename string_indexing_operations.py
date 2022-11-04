# Indexing Operator []

# you are going to learn Indexing now
#. Program should accept a string value while running
x=str(input("enter a string value=    "))
print("program is acceped the value you entered because it is string")
print(x)
print("you entered:   ", "'",x,"'")
# Find out first character in the string using string index

print("first charecter in   '",x,"' is", "'",x[0],"'")

# Find out last character in the string using string index

print("last charecter in   '",x,"'is", "'",x[-1],"'")

# Find out length of the string using “len” function and print the result

print("length of the string   '",x,"'is", len(x))

# Find out the middle character in the string using index

print("mid index is", len(x) // 2)

#a. If length of the string is an odd number print the middle character.

if len(x) % 2 != 0:
 print("middle character in   '",x,"'is", "'",x[int(len(x) / 2)],"'")

# b. If length of the string in an even number then print two of the middle characters
else:
 print("middle characters in   '",x,"' are", "'",x[int(len(x) // 2)],"'", "and", "'",x[int(len(x) // 2) + 1],"'")







