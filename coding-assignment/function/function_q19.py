def calculate_sum_of_cubes(n):
    """
    Problem 19: Write a function to calculate the sum of cubes of first n natural numbers.
    Input: n = 3
    Output: 36
    Explanation: 1^3 + 2^3 + 3^3 = 36.
    """
    return sum(i**3 for i in range(1, n + 1))