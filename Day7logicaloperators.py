# logical operators are used to combine conditional statements

# it includes the following operators:
# and = both conditions must be true
# or = at least one condition must be true
# not = reverse the result, returns false if the result is true

# the below is an exaple of how to use the and operator
temp = 30 

if temp < 30 and temp >0:
    print("it is a good day today")
else:
    print("it is a bad day today")


# the below is an exaple of how to use the or operator
temp = - 3 

if temp == 30 or temp >= 0:# only 1 condition needs to be true
    print("it is a good day today")
else:
    print("it is a bad day today")


# the below is an exaple of how to use the not operator
# not is a little bit diffirent 

sunny = True

if not sunny == True:# if you are working with a boolean you dont have to type sunny == True just sunny:
    print("it is sunny outside")
else:
    print("it is cloudy outside")
# not is use to change the boolean value if anser is true it will change it to false and if the answer is false it will change it to true