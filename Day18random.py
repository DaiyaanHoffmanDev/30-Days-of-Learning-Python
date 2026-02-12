import random

dice = random.randint(1,6)# random.randint = random whole numbers put in a range
print(dice)

# you can place variables as long as they can take numbers
high = 100
low = 1
high_or_low = random.randint(low, high)# remember the low must come first
print(high_or_low)

#random floating point number
random_float = random.random()
print(random_float)

#to choose a random choice
options = ("rock", "paper","scizzers")
rock_paper = random.choice(options)
print(rock_paper)

# to shuffle a list 
cards = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards)
print(cards)