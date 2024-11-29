def find_second_largest(lst):
    """
    Problem: Find the second largest element in a list.
    Input: [1, 3, 7, 2, 5]
    Output: 5
    Explanation: The largest is 7, and the second largest is 5.
    """
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None