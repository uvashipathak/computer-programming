def find_common_elements_in_tuples(tpl1, tpl2):
    """
    Problem 9: Find common elements in two tuples.
    Input: tpl1 = (1, 2, 3), tpl2 = (2, 3, 4)
    Output: (2, 3)
    Explanation: Elements 2 and 3 are common in both tuples.
    """
    return tuple(set(tpl1) & set(tpl2))