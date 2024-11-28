'''
Given a string. the task is to check if the string is symmetrical
 and palindrome or not. A string is said to be symmetrical if both 
 the halves of the string are the same and a string is said to be a 
 palindrome string if one half of the string is the reverse of the 
 other half or if a string appears the same when read forward or 
 backward.'''


def is_palindrome(s):
    return s == s[::-1]

def is_symmetrical(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]

string = "amaama"
if is_symmetrical(string):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if is_palindrome(string):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")