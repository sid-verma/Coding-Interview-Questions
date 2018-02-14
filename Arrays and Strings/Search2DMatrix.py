# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row. For example, consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

# KEY STEP: Binary Search in a slightly modified way.
# (1) Low and High are first and last elements respectively
# (2) Mid is middle of low, high. Convert it to [row, col] by [element no. / len(col), element no. % len(col)]
# (3) Check if else and assign new values to low and high respectively
# TC: O(log n)
# SC: O(1)

# *** MODIFIED QUESTION ***
# Note: If row and column are sorted in increasing order i.e the entire matrix is not a sorted list, then
# (1) Pick the top right element and check if equals target
# (2) If target is greater then move down. If matrix out of bounds, return false.
# (3) If target is lesser then move left. If matrix out of bounds, return false.
# TC: O(n)
# SC: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target == None:
            return False
        row, col = len(matrix), len(matrix[0])
        
        low, high = 0, row*col-1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid/col][mid%col]
            if num == target:
                return True
            if num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False