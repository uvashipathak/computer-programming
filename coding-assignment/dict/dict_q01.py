"""
@Hackerrank
Given  names and phone numbers, assemble a phone book that maps friends names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each  queried, print the
associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found,
print Not found instead.
"""

phone_book = {} #our phone book
n = int(input()) # Read the number of entries

# Populate the phone book
for _ in range(n):
    x = input().split()
    phone_book[x[0]] = x[1]

# Read queries and print results
try:
    while True:
        value = input()
        if value in phone_book:
            print(value + "=" + phone_book[value])
        else:
            print("Not found")
        if value == 'end':
            exit()
except EOFError:
    pass