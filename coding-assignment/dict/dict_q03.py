"""
@geeksforgeeks
Python | Sort Python Dictionaries by Key or Value
"""


class SortDict:
    """
    A class that provides static methods to sort dictionaries by keys or values.

    This class contains methods to sort a given dictionary either by its keys
    in ascending order or by its values in ascending order. The sorted output
    is returned as a new dictionary.
    """

    @staticmethod
    def sort_key(dictionary: dict) -> dict:
        """
        Sorts the given dictionary by its keys in ascending order.

        Parameters:
        ----------
        dictionary : dict
            The dictionary to be sorted. The keys must be comparable.

        Returns:
        -------
        dict
            A new dictionary sorted by keys in ascending order.
        """

        return dict(sorted(dictionary.items()))

    @staticmethod
    def sort_values(dictionary: dict) -> dict:
        """
        Sorts the given dictionary by its values in ascending order.

        Parameters:
        ----------
        dictionary : dict
            The dictionary to be sorted. The values must be comparable.

        Returns:
        -------
        dict
            A new dictionary sorted by values in ascending order.

        """

        return dict(sorted(dictionary.items(), key=lambda item: item[1]))