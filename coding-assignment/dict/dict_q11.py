"""
@geeksforgeeks
Given a dictionary, find the mean of all the values present.

Input : test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
Output : 4.0
Explanation : (4 + 4 + 4 + 4 + 4) / 4 = 4.0, hence mean.

Input : test_dict = {"Gfg" : 5, "is" : 10, "Best" : 15}
Output : 10.0
Explanation : Mean of these is 10.0
"""

def mean(test_dict: dict[object, int])-> float:
    """
    :param test_dict: dictionary whose mean is to be calculated
    :return: the mean of all the values present.
    """
    return sum(test_dict.values()) / len(test_dict)