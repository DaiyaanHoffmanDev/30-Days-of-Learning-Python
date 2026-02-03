# This is how the input function works in python
input("Enter your name:") # basic input function 

# storing the input into a variable
user_name = input("Enhter your name: ") # storing input in a variable
print(f"hello {user_name} how are you ") # using an f string to display the input

user_age = input("Enter your age: ") # or do it like this # user_age = int(input("enter your age: ")) to convert it directly to integer
user_age = int(user_age)
user_age = user_age + 1 # it will show an error if we do not convert the string to integer becouse you can not add integer to string
print(f"You are {user_age} years old")


#mad libs game exercise
noun = input("Enter a noun ")
adjective1 = input("Enter a adjective ")
verb = input("Enter a verb ")
adjective2 = input("Enter a adjective ")
adjective3 = input("Enter a adjective ")

print(f"i was playing playstation when a {noun} flew by {adjective1} ")
print(f"when a {noun} flew by it was {verb}ing ")
print(f" i was {adjective2} and as {adjective3} as a {noun}")

# Area of a rectangle calculator
# formula is length * width

length = int(input("Enter the length of the rectagle: "))
width = int(input("Enter the width of the rectangle: "))

Area = length * width 
print(f"the area of the rectangle is {Area} cm^2")


# shoping cart exercise
# how to make a simple shoping cart that takes user inputs
item = input("what would you like to buy: ")
price = float(input("what is the price of the item: "))
quantity = int(input("how much are you going to buy: "))

total = price * quantity 

print(f"You have bought {quantity} x {item}s")
print(f"You total price is R{round(total, 2)} ")# first time we learn this round function but we also learn that is we are in a f string and we use 1 function e.g round we use scwiggle y brackets but if we use 2 functions e.g round and str we use normal brackets
