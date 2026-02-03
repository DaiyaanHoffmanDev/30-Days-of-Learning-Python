import math

# the below is all about arithmetic operations and augmented assignments
items = 0


items = items + 1 # this is incremening 
items += 1 # also incrementing but less typing know as an augmented assignment 


items = items -1 # decrewmenting 
items -= 1 # same thing degramening less typing 


items = items / 1
items /= 1 # same thing as the above but less typing 

items = items * 1
items *= 1 # same thing as the above but less workds


items = items **2 # is to the power of 2
items **= 2 # same thing but is augmented assignment 

remainder = items % 2 # the % is moduler so basically devide an example to this is 13 devided by 3 is 4 with a remainder of 1 because 3 goes into 13 4 times and 1 is left over so the remainder is 1
# and and 10 % 2 is 0 because 2 goes into 10 5 times with no remainder
print(items)

# the below is about basic maths functions in python

x = 3.14 
y = -4
z = 5 

result = round(x) # built in round function
result = round(x, 1) # if you want to round to a certain point

result = abs(y)# abs is absolute value how far away is it from 0\
result = pow(5, 2)# built in power function so 5 * 5

result = max(x, y, z) # built in max function to get the highest value
result = min(x, y, z) # built in min function to get the lowest value


print(result)

# now we need to import the math module to use more complex math functions import it at the top of the text editor
print(math.pi) # this is how to use the math module to get pi value

# if you need the squere root of something
result = math.sqrt(items) # math.sqrt is the square root function
print(result)
result = math.ceil(x) # math.cell will always round a floating poiint number up
result = math.floor(x) # math.floor will always round a floating point number down


# calculate the cicumferance of a circle activity
# the formula is C = 2 * pi * r
import math
radius = float(input("enter the radius of a circle: "))

cir = 2 * math.pi * radius # using the math module to get a pi value 

print(f"the circumference of a circle is {round(cir, 2)}cm ")

# calculate the area of a circle 
# the formula is A = pi ^ r^2
import math

radius = float(input("enter the radius of the circle: "))

Area = math.pi * pow(radius, 2)

print(f"the area of a circle is {round(Area, 2)}cm^2 ")

# calculate the the hypotonues of a right angle triagle
# the formula is H = sqrt of a^2 + b^2
import math
a = float(input("enter the right side of the triangle: "))
b = float(input("enter the left side of the triangle: ") )

hypot = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"the hypotonues of a right angle triagle is {round(hypot, 2)}")

