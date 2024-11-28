"""
@geeksforgeeks
Given a string which contains lower alphabetic characters, we need to remove at most one character from this
string in such a way that frequency of each distinct character becomes same in the string.

Input  : str = “xyyz”
Output : True
We can remove character ’y’ from above
string to make the frequency of each
character same.

Input : str = “xyyzz”
Output : True
We can remove character ‘x’ from above
string to make the frequency of each
character same.

Input : str = “xxxxyyzz”
Output : False
It is not possible to make frequency of
each character same just by removing at
most one character from above string.
"""

from collections import Counter


def check_frequency(string: str)->bool:
    """
    :param string: String whose frequency is to be checked after removing at most one character
    :return: True if all characters have same frequency, false otherwise
    """
    freq = Counter(string)  # Frequency of each character
    freq_count = Counter(freq.values())  # Count occurrences of each frequency

    if len(freq_count) == 1:
        # All characters already have the same frequency
        return True
    elif len(freq_count) == 2:
        # Two distinct frequencies; check conditions
        (freq1, count1), (freq2, count2) = freq_count.items()
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            # One character with frequency 1 can be removed
            return True
        if abs(freq1 - freq2) == 1 and (count1 == 1 or count2 == 1):
            # One frequency can be reduced by 1 to match the other
            return True
    return False