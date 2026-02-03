# typecasting is converting one data type to anothe data type e.g string to integer , integer to float ect

# basic variables we are going to use for typecasting examples
name = "daiyaan" # string variable
age = 19 # interger variable
gpa = 3.5 # float variable\
is_student = True # boolean variable

# using the type() function to check the data type of the variables
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# lets try changing age from integer to float
age = float(age) # this is typecasting age from integer to float
print(age)

# same way if we do if from float to integer
gpa = int(gpa) 
print(gpa)
# we do the same for string to integer but the string must be a number in string form
# only exeption is boolean to integer and float it will always say true for any number but 0 even if the number is negative
age = bool(age)
print(age)

# it is useful to cast something as a boolean when cheaking if some put in there name when asked if it is empty if will say false and when it is not empty it will say true

# THE ABOVE IS EXAMPLES OF EXPLICIT TYPECASTING WHERE WE MANUALLY CHANGE THE DATA TYPE
# IMPLICIT TYPECASTING IS WHEN PYTHON AUTOMATICALLY CHANGES THE DATA TYPE FOR US
x = 5 # integer
y = 2.5 # float

z = x + y 
print(z) # here python automatically changed x from integer to float so that it can add it to y which is a float
print(type(z))