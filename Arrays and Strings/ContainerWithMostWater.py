# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# Key Step: i = 0, j = last, check which one is smaller and either increment or decrement. Take the max area.
# TC: O(n)
# SC: O(1)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        i = 0
        j = len(height)-1
        area = min(height[i], height[j]) * (j-i)
        while i!= j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            area = max(area, min(height[i], height[j]) * (j - i))
            
        return area

obj = Solution()
print(obj.maxArea([2,6,5,8,3,4,8,9,3,1]))