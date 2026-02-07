#while loops executes a block of code as long as a condition is true

name = input("Enter your name: ")

while name == "":# while name is emputy print the first line if its not empty move on 
    print("You did not enter a name:")# print this line if the name is empty
    name = input("Enter your name: ")# ask for the name again if the name is empty, this is also here then the code doesnt break 
    print(f"hello {name} how are you")# print this line if the name is not empty

    age = int(input("Enter your age: "))

while age <= 0:
    print("Your did not enter a valid age")
    age = int(input("enter your age: "))
    
print(f"Your age is {age} years old ")

# how to exit a while loop
food = input("Enter a food you like (q to quit): ")

while not food == "q":# while food is not equal to q print the first line if its equal to q exit the loop and print bye
    print(f"you like {food} ")
    food = input("Enter a food you like (q to quit): ")

print("bye")

num = int(input("type a number from 1 to 10: "))

while num <= 0 or num > 10:
    print("that is not a valid number: ")
    num = int(input("type a number from 1 to 10: "))
    
print(f"Your number is {num} ")