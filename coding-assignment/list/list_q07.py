def group_elements_by_frequency(lst):
    """
    Problem: Group elements by their frequency.
    Input: [4, 5, 6, 5, 4, 3]
    Output: [[4, 4], [5, 5], [6], [3]]
    Explanation: Elements with the same frequency are grouped together.
    """
    from collections import Counter
    freq = Counter(lst)
    return [[key] * freq[key] for key in freq]