# string indexing is used to access individual characters in a string. In Python, strings are indexed starting from 0. This means that the first character of a string is at index 0, the second character is at index 1, and so on.

# indexing = accessing elements of a sequence using the [] the idecing operator 
# [strart:end:step]

card_number = "1234 5678 9012 3456"

print(card_number[3]) # this will print the character at position 3 which is '4'
print(card_number[0: 6])# [start:end] you can also do it like this [:6] does the same things 
print(card_number[5:9]) # this will start form position 5 and end at 9
print(card_number[5:]) # this will start at 5 and print until the end of the string
print(card_number[-1]) # this will print the last character of the string which is '6'
print(card_number[-3:]) # this will print the last three characters of the string which is '456'
print(card_number[:-1]) # this will print the string except the last character
print(card_number[::2]) # this will print every second character in the string
# now step 
print(card_number[::3]) # this will print every third character in the string
print(card_number[::-1]) # this will print the string in reverse order
#[::] putting nothing in start and end will take the entire string

#excercise print last 4 characters of the string
card_number = "1234 5678 9012 3456"
last_4digits = card_number[-4:]
print(f"the last 4 digits are {last_4digits}")

#This is how to reverse the string
card_number = "1234 5678 9012 3456"
card_number = card_number[::-1]#nothing mean all
print(f"this is the card number reversed {card_number}")