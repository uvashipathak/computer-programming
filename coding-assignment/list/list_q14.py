def is_list_palindrome(lst):
    """
    Problem: Check if a list is a palindrome.
    Input: [1, 2, 3, 2, 1]
    Output: True
    Explanation: The list reads the same backward as forward.
    """
    return lst == lst[::-1]