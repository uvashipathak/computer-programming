"""
@geeksforgeeks
Given a list of elements, perform grouping of similar elements, as different key-value lists in a dictionary.

Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
Explanation : Similar items grouped together on occurrences.

Input : test_list = [7, 7, 7, 7]
Output : {7 : [7, 7, 7, 7]}
Explanation : Similar items grouped together on occurrences.
"""

def group_elements(test_list: list[int]) -> dict[int, int]:
    """
    :param test_list:
        list of integers to group together
    :return:
        a dictionary of the integers grouped together
    """
    res = {}
    for i in test_list:
        res[i] = res.get(i, 0) + 1
    return res