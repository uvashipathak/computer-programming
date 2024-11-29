def generate_fibonacci_series(n):
    """
    Problem 3: Generate the first n Fibonacci numbers using a function.
    Input: n = 6
    Output: [0, 1, 1, 2, 3, 5]
    Explanation: The first six Fibonacci numbers are generated.
    """
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series