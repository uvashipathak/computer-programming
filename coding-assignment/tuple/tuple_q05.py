def merge_two_tuples_alternating(tpl1, tpl2):
    """
    Problem 5: Merge two tuples by alternating their elements.
    Input: tpl1 = (1, 3, 5), tpl2 = (2, 4, 6)
    Output: (1, 2, 3, 4, 5, 6)
    Explanation: Elements from both tuples are interwoven alternately.
    """
    return tuple(x for pair in zip(tpl1, tpl2) for x in pair)