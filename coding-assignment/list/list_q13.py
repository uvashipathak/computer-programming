def calculate_running_sum(lst):
    """
    Problem: Calculate the running sum of a list.
    Input: [1, 2, 3, 4]
    Output: [1, 3, 6, 10]
    Explanation: Each element is the sum of all previous elements and itself.
    """
    running_sum = []
    current_sum = 0
    for num in lst:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum