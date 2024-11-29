def find_longest_consecutive_sequence(lst):
    """
    Problem: Find the longest consecutive sequence in a list.
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence is [1, 2, 3, 4], length 4.
    """
    nums = set(lst)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest