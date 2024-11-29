def rotate_list(lst, k):
    """
    Problem: Rotate a list to the right by k steps.
    Input: lst = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]
    Explanation: The list is rotated so that the last 2 elements come to the front.
    """
    k %= len(lst)
    return lst[-k:] + lst[:-k]