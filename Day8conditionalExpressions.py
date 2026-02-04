# a conditional ecpression is a way to shorten an if else statement into a single line also called a ternary operator

num = 5

print("positive" if num > 0 else "negitive") # put an if else statement in a single line

result = 10

print("even" if result % 2 else "odd") # if the result is even it will print even if the result is odd it will print odd


a = float(input("enter a number: ")) # doesnt have to be a float i was just bored so i did extra stuff to make it more interesting you can just use int if you want to work with whole numbers or you dont have to a function at all if you just want to use numbers in the code without user input
b = float(input("enter another number: "))

max_num = a if a > b else b # the if statement is shorter like this instead of writing a full if else statement to find the bigger number between a and b we can write it in one line like this

print(f"the bigger number between the 2 is {max_num}")# just added extra stuff to make sure i understand how to use the conditional expression in a more complex way you can just print max_num if you want to keep it simple

user_role = "admin" # another good example

access_level = "full access" if user_role == "admin" else "limit access" # dont make the mistake of putting a is operator it else directly after the conditional expression it will cause an error

print(access_level)