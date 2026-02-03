# variable are reusable container to store data values in there are 4 basic types of variable  in python e.g string, interger, float, boolean

#Learning String variables
first_name = "daiyaan"
food = "pasta"
print(first_name) # normal variable
print(f"hello {first_name}") # this is an f string variable f stands for format
print(f"You like eating {food}" +" "+ f"Your name is {first_name}") # learning f string with variable
print("hello " + first_name + " you like eating " + food) # this is the same thing without f string

#Learning Integer variables
age = 19 # should not be in quotes because then it will be a string variable
# other examples of integer variables are height, weight, year , quantity bassically whole numbers
print(f"you are {age} years old")

# Learning Float variables
price = 99.99 # float varable should have a decimal points 
# float variabhle are basically any number with decimal points like weight in kgs, height in meters , price of an item etc
print (f"the price of a box of pasta is R{price} for a box of 5x9 packs")

# Learning Boolean variables
is_tired = True # boolean vcariable are either true or false
# its just basicly a yes or no question
print(f"you worked all day are you tired? {is_tired}")\


# EXTRS STUFF THAT IS NOT NESSARY RIGHT NOW
# boolean variable are normally tied to if statements and loops which we will learn later
# but it basically goes like this
is_for_sale = False
if is_for_sale: # we will work and learn more about if statements later
    print("this car is for sale")
else:
    print("this car is not for sale")

