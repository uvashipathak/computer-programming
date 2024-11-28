#Check if a String is a Valid Email
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Example
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))     # Output: False
