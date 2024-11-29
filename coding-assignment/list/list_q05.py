def flatten_nested_list(nested_lst):
    """
    Problem: Flatten a nested list.
    Input: [[1, 2, [3]], 4]
    Output: [1, 2, 3, 4]
    Explanation: The nested elements are flattened into a single list.
    """
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    return list(flatten(nested_lst))