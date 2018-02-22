# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6

# Example 2:
# Input: [1,2,3,4]
# Output: 24

# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# KEY STEP:
# The max can be the maximum either
# - The three max numbers
# - The max number and two min numbers (since three min numbers would either give min or negative).

import sys
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        max1 = max2 = max3 = -1 * sys.maxsize
        min1 = min2 = sys.maxsize
        
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:

                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return max(max1 * max2 * max3, max1 * min1 * min2)

