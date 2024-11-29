def find_majority_element(lst):
    """
    Problem: Find the majority element in a list.
    Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
    Output: 4
    Explanation: A majority element is one that appears more than n // 2 times.
    """
    from collections import Counter
    n = len(lst)
    count = Counter(lst)
    for key, value in count.items():
        if value > n // 2:
            return key
    return None  # No majority element