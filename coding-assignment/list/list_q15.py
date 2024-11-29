
def find_pairs_with_sum(lst, target_sum):
    """
    Problem: Find all pairs of numbers in a list that add up to a target sum.
    Input: lst = [1, 2, 3, 4, 5], target_sum = 6
    Output: [(1, 5), (2, 4)]
    Explanation: Pairs (1, 5) and (2, 4) sum to 6.
    """
    seen = set()
    pairs = []
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs