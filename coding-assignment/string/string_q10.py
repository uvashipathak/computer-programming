#3. Count the Frequency of Each Character
from collections import Counter

def char_frequency(s):
    return Counter(s)

# Example
print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
