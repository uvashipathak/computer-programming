def split_list_by_condition(lst, condition):
    """
    Problem: Split a list into two based on a condition.
    Input: lst = [1, 2, 3, 4], condition = lambda x: x % 2 == 0
    Output: ([2, 4], [1, 3])
    Explanation: The first list contains elements satisfying the condition, the second does not.
    """
    pass_list = [x for x in lst if condition(x)]
    fail_list = [x for x in lst if not condition(x)]
    return pass_list, fail_list