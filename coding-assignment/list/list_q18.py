def merge_sorted_lists(lst1, lst2):
    """
    Problem: Merge two sorted lists into a single sorted list.
    Input: lst1 = [1, 3, 5], lst2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]
    Explanation: The two lists are merged and sorted.
    """
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result