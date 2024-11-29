def remove_duplicates(lst):
    """
    Problem: Remove duplicates from a list while maintaining order.
    Input: [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]
    Explanation: Only unique elements are kept in their original order.
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
