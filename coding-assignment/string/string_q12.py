# Check if Two Strings are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example
print(are_anagrams("listen", "silent"))  # Output: True
