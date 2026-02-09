# collections = single variables used to store multiple values
# list = [] ordered and changeable duplicates ok
# set = {} unordered and immutable but add and remove ok no duplicated
# Tuple = () ordered and unchangeable duplicates ok and faster
# you can also use the index operator [start:end:step]

# list 
fruits = ["apple", "bananna", "orange", "grapes"]
print(fruits[0])# you put [] to access 1 of the values in this case 0 to 3 python start @ 0
# you can also use a for loop
for i in fruits:
    print(i)

dir(fruits)# if you print this it shows the different methods available to a function

print("apple" in fruits)# you can use the in operator so see if an item is in a list

fruits[0] = "coconut" # to change what is in value 0 to coconut
print(fruits)

fruits.append("pineapple")# use append method to add things to the list
print(fruits)

fruits.remove("bananna")# used to remove from a list
print(fruits)

fruits.insert(0, "apple")# this will put a item in index without replacing it 
print(fruits)

fruits.sort()# puts the list in alphabetincle order
print(fruits)

fruits.reverse()# if its is sorted first then revesed its revesed alpha order if not then its reversed the order given
print(fruits)


print(fruits.index("apple"))# show at what index the word " apple " is placed  btw it is index 4 becouse we revesed to listw

print(fruits.count("apple"))# counts how much times an item appears in a list


fruits.clear()# to clear the list 
print(fruits)

# sets we cant alter these values and everytime you run its in a different order
cars = {"polo", "porshe", "mustang", "mazda"}# the same stuff that applies for list applies here we are not able to use indexing on a set becuase its random each time 
cars.add("toyota")# adds the "" to the set
cars.pop()# removes whatever element is first but its random
print(cars)

# Tuples




