#4. Find the First Non-Repeating Character
def first_non_repeating(s):
    freq = s.count()
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example
print(first_non_repeating("swiss"))  # Output: "w"
