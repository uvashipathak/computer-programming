def flatten_nested_tuple(nested_tpl):
    """
    Problem 8: Flatten a nested tuple.
    Input: nested_tpl = ((1, 2), (3, 4), (5,))
    Output: (1, 2, 3, 4, 5)
    Explanation: All elements from the nested structure are combined into a single tuple.
    """
    def flatten(tpl):
        for item in tpl:
            if isinstance(item, tuple):
                yield from flatten(item)
            else:
                yield item
    return tuple(flatten(nested_tpl))