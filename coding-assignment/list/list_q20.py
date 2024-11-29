def generate_all_permutations(lst):
    """
    Problem: Generate all permutations of a list.
    Input: [1, 2, 3]
    Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    Explanation: The output contains all possible orderings of the elements in the list.
    """
    from itertools import permutations
    return list(map(list, permutations(lst)))