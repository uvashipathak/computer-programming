def find_missing_number(lst, n):
    """
    Problem: Find the missing number in a list of integers from 1 to n.
    Input: lst = [1, 2, 4, 5], n = 5
    Output: 3
    Explanation: The number 3 is missing in the range 1 to 5.
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum