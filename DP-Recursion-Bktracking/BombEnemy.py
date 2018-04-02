# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# KEY STEP: Parse the matrix in row major form.
# For each row streak, compute the rowHits and the colHits.
# Note: Since we are parsing in row major, we need to store the number of colHits in an array as per index, and update only if we meet a wall.
# If the matrix cell is at a '0', then update the result as max of current or rowHits + colHits[j]

# TC: O(mn)
# SC: O(n)

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        result = rowhits = 0
        colhits = [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        rowhits += grid[i][k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colhits[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, rowhits + colhits[j])
        return result  