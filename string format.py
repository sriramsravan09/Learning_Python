#https://www.youtube.com/watch?v=fy10ci10R_g&ab_channel=JoeJames

#String formatting is also known as String interpolation. It is the process of inserting a custom string or variable in predefined text.
#Methods for Formatting
#Positional formatting
#Formatted string literals
#Template method


# replacing the position of the string
first_name="sravan"
last_name="sriram"
print ("13 my name is {}" .format(first_name))
print ("14 my name is {} {}".format(first_name,last_name))

#replacing string using index
print("17 my name is {0},{1}".format(last_name,first_name))
print("18 my name is {0} {1}. last name is {0}".format(last_name,first_name))

# allignment: left={} or {:<}, right={:>n}, middle={:^n}
# n= number of spaces you want
marks=[36, 90, 28, 72, 88]
for mark in marks:
    print("24 marks of the student  are: {}".format(mark))
    #right allignment{:>n}
for mark in marks:
    print("27 marks of the student are: {:>5}".format(mark))
