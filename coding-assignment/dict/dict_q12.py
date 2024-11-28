"""
@geeksforgeeks
Given two strings, find if we can make first string from second by deleting some characters from second and
rearranging remaining characters.

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : True

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : False

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : True
"""
from collections import Counter


def make_string(shorter: str, longer:str) -> bool:
    """
    :param shorter: The string that's to be made from the longer one
    :param longer:  The sting whose characters we will rearrange and delete to make the shorter one
    :return: True if we can make the shorter string from longer, else False
    """
    s1 = Counter(shorter)
    s2 = Counter(longer)
    for i in s1.keys():
        if i not in s2.keys() or s1[i] > s2[i]:
            return False
    return True

print(make_string('GeeksforGeeks', 'rteksfoGrdsskGeggehes'))
