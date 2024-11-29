def swap_first_last_elements(tpl):
    """
    Problem 1: Swap the first and last elements of a tuple.
    Input: tpl = (1, 2, 3, 4)
    Output: (4, 2, 3, 1)
    Explanation: The first element (1) and last element (4) are swapped.
    """
    if len(tpl) < 2:
        return tpl
    return (tpl[-1],) + tpl[1:-1] + (tpl[0],)
