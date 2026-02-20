#defualt argument is a defualy value for a certain parameters it is used when that argument is not passed if makes your function more flexible reduces number of lines of code and makes your code more readable,and number of arguments 1:positional, 2:default , 3:keywords, 4: arguments

def net_price(list_price, discount=0, tax=0.05):# the default values are discount and tax
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))# we only used passed 1 parameter and it doesnt give an error
print(net_price(500,0.1))# we pass 2 parameter and it replaces the default value
print(net_price(500,0.1,0))# all parameters are passed 

# versions of the activity

def user_time(hours=0,minutes=0,seconds=0):
    print(f"hours{hours:02},minutes{minutes:02},seconds{seconds:02}")
    
user_time(1,23,70)# putting the parameters
user_time(seconds=30)# just testing 

# activity answer
import time
def count(end, start=0):# put the end time first decause the default argument must come after or it will give an error 
    for i in range(start, end+1):# we +1 becouse it inclusive
        time.sleep(1)
        print(i)
    print("finished")

count(10)# only put the end time

# bonus acitvity my answer
def greet(name,status="guest"):
    print(f"hello {name},you are logged in as {status}")


greet("daiyaan")# testing if this works withour another paraminter
greet("daiyaan","admin")# have to put "" then python doesnt look for variables called daiyaan

# my answer is actually correct no need for the other solution