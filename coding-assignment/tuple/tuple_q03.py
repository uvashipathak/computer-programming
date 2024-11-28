def find_index_of_element(tpl, element):
    """
    Problem 3: Find the index of a specific element in a tuple.
    Input: tpl = (10, 20, 30, 40), element = 30
    Output: 2
    Explanation: The element 30 is at index 2.
    """
    return tpl.index(element) if element in tpl else -1