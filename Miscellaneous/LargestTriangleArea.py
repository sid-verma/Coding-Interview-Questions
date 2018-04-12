# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2

# KEY STEP: Brute Force check using Heron's Formula or Shoelace Formula.

# Area of triangle is given by square around it - 3 right angled triangles
#           | 1    1   1 |
# A = 0.5 * | x1  x2  x3 |
#           | y1  y2  y3 |

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1, p2, p3):
            if len(p1) != 2 or len(p2) != 2 or len(p3) != 2 or (p1[1] == p2[1] == p3[1]) or (p1[0] == p2[0] == p3[0]):
                return 0
            return 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p2[0]*p1[1] - p3[0]*p2[1] - p1[0]*p3[1])
                        
        maxArea = 0
        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    maxArea = max(maxArea, area(points[i], points[j], points[k]))
        return maxArea