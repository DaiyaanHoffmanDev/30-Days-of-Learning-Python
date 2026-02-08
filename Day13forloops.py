# for loops = exacute a block of code a limited amount of times this can be itaralted as a range ,string , sequence etc

for i in range(1, 11):# this counts to 10
    print(i)
print("Happy New Year")

# to count from 10 to 1 we can use the reverse function
for i in reversed(range(1, 11)):# you can also use the step function remember day 12 while loops
    print(i)
print("Happy New Year")

for i in range(1,11):# this is using the continue to skip the number 5 
    if i == 5:
        continue
    print(i)

for i in range(1,11):# this uses the break function to stop the code at 5
    if i == 5:
        break
    print(i)