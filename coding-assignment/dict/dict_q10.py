"""
@geeksforgeeks
Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the
string in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Input : N = 3
        paradox
Output : paizwlc
Explanation: We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pneumlmrz
"""

def mirror(string: str, from_char: int=0) -> str:
    """
    :param string: String to be mirrored
    :param from_char: Character at which to start mirroring
    :return: String mirrored
    """
    mirror_dict = dict(zip('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
    return string[:from_char] + ''.join([mirror_dict[i] for i in string[from_char:]])