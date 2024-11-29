def find_intersection_of_two_lists(lst1, lst2):
    """
    Problem: Find the intersection of two lists.
    Input: lst1 = [1, 2, 2, 3], lst2 = [2, 3, 4]
    Output: [2, 3]
    Explanation: The intersection contains elements that appear in both lists, without duplicates.
    """
    return list(set(lst1) & set(lst2))