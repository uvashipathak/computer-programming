def find_lcm(a, b):
    """
    Problem 7: Write a function to find the LCM of two numbers.
    Input: a = 12, b = 15
    Output: 60
    Explanation: The least common multiple of 12 and 15 is 60.
    """
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)