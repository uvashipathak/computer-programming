"""
@geksforgeeks
Merge two dictionaries into a single dictionary.
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Parameters:
    ----------
    dict1 : dict
        The first dictionary to merge.
    dict2 : dict
        The second dictionary to merge.

    Returns:
    -------
    dict
        A new dictionary containing the merged key-value pairs from both
        input dictionaries.
    """
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary
    return merged_dict
