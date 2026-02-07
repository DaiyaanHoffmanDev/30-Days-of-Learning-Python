# format specifiers = {value:flag} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"the price 1 R{price1:.2f}")# specifier is after the colon and the the . e.g :.2f f = float
print(f"the price 2 R{price2:.2f}")
print(f"the price 3 R{price3:.2f}")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"the price 1 R{price1:10}")#this adds 10 spaces to the right of the value
print(f"the price 2 R{price2:<10}")# this adds 10 spaces to the left of the value
print(f"the price 3 R{price3:^10}")# this adds 10 spaces to the left and right of the value and centers it in the middle of the spaces

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"the price 1 R{price1:+,}")#this adds a comma as a thousand separator
print(f"the price 2 R{price2:+,.2f}")# this will add a comma as a thousand separator and also round the value to 2 decimal places
print(f"the price 3 R{price3:+,}") # the plus sign will add a plus sign to the value if it is positive and a minus sign if it is negative

