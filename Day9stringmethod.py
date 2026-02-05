name = input("Enter your name: ")
result = len(name)# the len function will give use the length of a string how much charactors including spaces
result = result - 1 # or result -= 1
print(result)

name  = input("Enter you name: ")

result = name.find(" ")# find method will return the first occurence of a give charactor in this case it is a space using a . symbol
print(result)

name  = input("Enter you name: ")

result = name.rfind(" ")# the rfind method will return the last occurence of a give charactor in this case it is a space using a . symbol with rfind if there are no results it will return -1
print(result)

name  = input("Enter you name: ")

name = name.capitalize()# this will make the fitst letter capital
print(name)

name  = input("Enter you name: ")
name = name.upper()# this will make all the letters uppercase
name = name.lower()# this will make all the letters lowercase
name = name.isdigit()# this will check if all the charactors in the string are all digits and it will return a boolean value true or false
result = name.isalpha()# this will check if all the charactors in the string are all letters and it will return a boolean value true or false
print(name)

phone_number = input("Enter your phone number: ")

phone_number = phone_number.isdigit()# is true cause phone number is only numbers
print(phone_number)

phone_number = input("Enter your phone number: ")

phone_number = phone_number.count("-")# count method counts what ever you specify
print(phone_number)

phone_number = input("Enter your phone number: ")

phone_number = phone_number.replace(" ", "-")# the replace method will replace what you specify with what you want
print(phone_number)

# print(help(str))# if you want to see the string methods

# usefull to remeber string methods:
# length = len(name)
# index = name.find(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count(" ")
# phone_number = phone_number.replace("-", "")

# exercise username cant be more than 12 charactors and it cant contain spaces or numbers
user_name = input("Enter your username: ")

if len(user_name) > 12:
    print("Username cant be more than 12 charactors")
elif user_name.find(" ") > 0:
    print("Username cant contain spaces")
elif not user_name.isalpha():
    print("Username cant contain numbers")
else:
    print("Username is valid")