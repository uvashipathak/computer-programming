"""
@GeeksforGeeks
Python program to find the sum of all items in a dictionary.

Input:
    line 1: {'a': 1, 'b': 2, 'c': 3}
    line 2: ['a', 'b']
Output:
    3
Explanation:
    a + b
"""

def sum_of_items(dictionary: dict, li: list = None) -> int:
    """
    Calculate the sum of specified items in a dictionary.

    Parameters:
    ----------
    dictionary : dict
        A dictionary containing key-value pairs where values are numeric.
    li : list, optional
        A list of keys to sum. If None, all keys in the dictionary are summed.

    Returns:
    -------
    int
        The sum of the values corresponding to the specified keys.
    """
    if li is None:
        li = dictionary.keys()
    sum_dict = 0
    for i in li:
        if i in dictionary:
            sum_dict += dictionary[i]
    return sum_dict