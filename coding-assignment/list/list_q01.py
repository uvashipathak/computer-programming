"""
@leetcode
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's
elements using the operation mentioned above.
"""


class Solution:
    """My Solution"""
    @staticmethod
    def max_matrix_sum(matrix: list[list[int]]) -> int:
        """
        Intuition: If there are an even no. of negative elements, all of them can be flipped and hence the max
        sum would be the same as the absolute sum of the matrix
        If there are an odd no. of negative elements, all of them but one can be flipped and hence the max sum
        would be the absolute sum of the matrix - twice the smallest element of the matrix, once because we
        couldn't add it to the matrix and once because we have to subtract it from the matrix
        """
        int_min = 100000 #The maximum value of a matrix element was 10^5, so the minimum value by default was set to that
        neg_count = 0 #neg_count counts the amount of negative elements
        sum_matrix = 0 #sum_matrix calculates the absolute sum of the matrix

        for i in matrix:
            for j in i: #looping through each element of the matrix
                if j < 0: #update the value of neg_count and flip the value
                    neg_count += 1
                    j = -j
                sum_matrix += j #update the absolute sum
                if j < int_min: #this calculates the smallest element of the matrix
                    int_min = j
        if neg_count % 2 == 0:
            return sum_matrix #no need to subtract twice of int_min as all elements can be flipped
        return sum_matrix - (2 * int_min) #We need to subtract 2*int_min
