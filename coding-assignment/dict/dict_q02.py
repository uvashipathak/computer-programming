"""
@geeksforgeeks
Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary
as value.

Input : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]
Output : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}
Explanation : Index-wise key-value pairing from list [8] to dict {‘Gfg’ : 4} and so on.

Input : test_dict = {‘Gfg’ : 4}, test_list = [8]
Output : {8: {‘Gfg’: 4}}
Explanation : Index-wise key-value pairing from list [8] to dict {‘Gfg’ : 4}.
"""


class Solution:
    """
    A class to provide a solution for creating a nested dictionary
    from a given list and dictionary.

    Methods
    -------
    nested_dict_from_list(test_dict, test_list):
        Creates a nested dictionary by mapping each element of the list
        to the corresponding item in the dictionary based on their indices.
    """

    @staticmethod
    def nested_dict_from_list(test_dict, test_list):
        """
        Creates a nested dictionary by mapping each element of the list
        to the corresponding item in the dictionary based on their indices.

        Parameters
        ----------
        test_dict : dict
            A dictionary where keys are strings and values are integers.
        test_list : list
            A list of integers to be used as keys in the nested dictionary.

        Returns
        -------
        dict
            A nested dictionary where each key is an element from the list,
            and each value is a dictionary containing a single key-value pair
            from the input dictionary, based on the index.

        Raises
        ------
        IndexError
            If the length of the list is greater than the length of the dictionary.

        """
        nested_dict = {}
        for i, j in zip(test_list, test_dict):
            nested_dict[i] = {j: test_dict[j]}

        return nested_dict