def tuple_to_dict(tpl):
    """
    Problem 10: Convert a tuple of key-value pairs into a dictionary.
    Input: tpl = (('a', 1), ('b', 2), ('c', 3))
    Output: {'a': 1, 'b': 2, 'c': 3}
    Explanation: Each pair in the tuple is treated as a key-value pair in the dictionary.
    """
    return dict(tpl)