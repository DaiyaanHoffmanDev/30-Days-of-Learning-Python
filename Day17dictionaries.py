capital = {
    "france": "paris",
    "germany": "berlin",
    "italy": "rome",
    "england": "london"}

print(capital.get("france"))

if capital.get("italy"):
    print("that capital is in the list")
else:
    print("that capital is not in the list")
    
capital.update({"south africa": "cape town"})

print(capital)

#change a value
capital.update({"south africa": "china"})

print(capital)

# to delete a vaule 

capital.pop("england")# dont add the {} braces
print(capital)

capital.popitem()# this removes the latest item
print(capital)

# to get the teys in a dictionary only the first part of each
keys = capital.keys()
print(keys)
for i in keys:
    print(i)
    
# to get the other part of dict e.g values 

values = capital.values()
print(values)
for i in values:
    print(i)
    
items = capital.items()
print(items)

#show everything in the dict
for key, value in capital.items():
    print(f"{key}, {value}")

# clear the dictionary
capital.clear()
print(capital)