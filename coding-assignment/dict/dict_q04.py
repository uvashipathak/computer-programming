"""
@GeeksforGeeks
Handling missing keys in Python dictionaries
"""

class MyDict(dict):
    """
    A custom dictionary class that extends the built-in `dict` to handle
    missing keys gracefully.

    This class overrides the `__missing__` method to provide a custom
    response when a requested key is not found in the dictionary. Instead of
    raising a KeyError, it returns a user-defined message indicating that the
    key was not found.
    """

    def __missing__(self, key):
        """
        This method is called by the dictionary when a key is not found.

        Parameters:
        ----------
        key : Any
            The key that was requested but not found in the dictionary.

        Returns:
        -------
        str
            A string message indicating that the key was not found.
        """
        return f'{key} Not Found'