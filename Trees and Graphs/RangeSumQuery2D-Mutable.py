# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [[3, 0, 1, 4, 2],
#   			  [5, 6, 3, 2, 1],
#   			  [1, 2, 0, 1, 5],
#   			  [4, 1, 0, 1, 7],
#   			  [1, 0, 3, 0, 5]]
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

# KEY STEP: Implement using Binary Index Tree of size (m+1,n+1) if matrix size is (m,n)
# Things to remember in Binary Index Tree
# - Getting next node from current node i = i + 2's complement of i = i + i & (-i)
# - Getting parent node from child node i =	i - 2's complement of i = i - i & (-i)

# TC: Creating 1st time O(n log n)^2 since it's 2D
#	  Updating O(log n)^2 since it's 2D
#     Calculating Sum O(log n)^2 since it's 2D

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prevVal = [[0]*self.n for i in range(self.m)]
        self.BITree = [[0]*(self.n+1) for i in range(self.m+1)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
                
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0:
            return
        
        diff = val - self.prevVal[row][col]
        self.prevVal[row][col] = val
        
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.BITree[i][j] += diff
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        def sumUpto(row, col):
            total = 0
            i = row
            while i > 0:
                j = col
                while j > 0:
                    total += self.BITree[i][j]
                    j -= j & (-j)
                i -= i & (-i)
            return total
                    
        if self.m == 0 or self.n == 0:
            return 0
        return sumUpto(row2+1, col2+1) + sumUpto(row1, col1) - sumUpto(row1, col2+1) - sumUpto(row2+1, col1)
