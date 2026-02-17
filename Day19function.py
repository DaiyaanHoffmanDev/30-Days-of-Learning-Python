#functions are reusable blocks of code place () after the function name is called a parameter

def happy_birthday(name, age):# the parameter is whats in  () this it has to match when you call the function and its like a temp variable 
    print(f"happy birthday to {name}")# you can invock a function 
    print(f"how old are you {age}")
    print(f"happy birthday to you")
    
happy_birthday("daiyaan", "20")
happy_birthday("kanyan", "19")
happy_birthday("adityya", "33")

def invoice_date(username, due_date, ammount):
    print(f"hello MR.{username}")
    print(f"you payment is due on {due_date}")
    print(f"your ammount due is {ammount}")

invoice_date("Hoffman", "21/12/2027", 2000)

# return functions is used to end a function and return a value

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

print(add(20,25))
print(sub(30,10))
print(mult(50,2))
print(div(50,2))


def create_full_name(name, surname,):
    name = name.capitalize()
    surname = surname.capitalize()
    return name + " " + surname
    
full_name = create_full_name("daiyaan", "hoffman")
print(full_name)