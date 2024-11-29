def generate_power_set(lst):
    """
    Problem: Generate the power set of a list.
    Input: [1, 2]
    Output: [[], [1], [2], [1, 2]]
    Explanation: The power set is all possible subsets of the list.
    """
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst) + 1)))
