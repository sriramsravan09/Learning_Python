#ask user to enter the value from which number he wants to print even number
A=int(input("Enter a number    "))
#display the number what user entered
print(" You entered  <",A,">")
#ask user how many even numbers he want to display from the number he entered
B=int(input("How many even numbers you want to print?   "))
# display the user how many enen numbers are going to be printed
print("printing", B, "even numbers after", A)
#formula to obtain till nth number
C=2*B+1
#range is from A to C; C=nth number which user desided to display those many even bumbers
for i in range(A,C):
 #formula for a number to be called even number
 if i % 2 == 0:
  #print the requested numbers
  print(i)





