# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. 
# Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

# KEY STEP: DFS
# - Check whether row, col is in limits and value is 1.
# - If true, set value to 0 (sink island) and call 4 directions recursively
# - Else return 0
# - Loop through i, j and find max area.

# TC: O(R x C)
# SC: O(R x C)
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def area(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return (1 + area(i-1, j) + area(i+1, j) + area(i, j-1) + area(i, j+1))
            return 0
        
        mA = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    mA = max(area(i,j), mA)
        return mA