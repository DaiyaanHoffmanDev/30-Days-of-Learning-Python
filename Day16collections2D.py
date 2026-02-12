# 2D collections for tuples, sets and lists , it is a collection made up of collections

fruits = ["apple", "orange", "grape"]
vegetables = ["carrot", "potatoe", "onion"]
meats = ["chicken", "beef", "fish"]

groceries1 = [["apple", "orange", "grape"], ["carrot", "potatoe", "onion"],["chicken", "beef", "fish"]]


print(groceries1)# this just gives everything
print(groceries1[0])# this just gives everything from the first list 
print(groceries1[0][1])# this only gives 1 item from index 0 the item is indexed 1

for collections in groceries1:
    print(collections) # this prints the entire list
    
    
for collections in groceries1:
    for items in collections:
        print(items, end=" ")


fruits[0] = "pineapple" # this will change the first item in the list
groceries = [fruits, vegetables, meats]
 
print(groceries)# this just gives everything
print(groceries[0])# this just gives everything from the first list 
print(groceries[0][1])# this only gives 1 item from index 0 the item is indexed 1 

#excercise make a keypad use tuple Bcause tuples are unchangeable
num_pad = ((" 1 ", " 2 ", " 3 "),(" 4 ", " 5 ", " 6 "),(" 7 ", " 8 ", " 9 "))

for num in num_pad:
    for row in num:
        print(row, end= "")
    print()