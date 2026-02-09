#it is the loop found in the code of another loop 
# while loop inside a while loop , for loop inside a for loop , while loop inside a for loop and for loop inside a while loop

for i in range(1, 11):
    print(i, end = "-")# the end = "" is used to print the numbers in the same line and you can add a spade or any other character in the end = "" to separate the numbers

# if you want to print the for loop 3 times you can use another for loop to do that

for i in range(3): # the counter e.g i should not be the same as the counter of the inner loop
    for j in range(1, 11):# couter of the inner loop is changed to j to avoid confusion with the counter of the outer loop
        print(j, end = "")
    print()# this is used to print a new line after each iteration of the outer loop

# lets make a rectangle using nested loops

row = int(input("enter the ammount of rows: "))
columns = int(input("enter the amount of columns: "))
symbol = input("enter the synbol to use: ")

for i in range(row):
    for j in range(columns):
        print(symbol, end = "")
    print()