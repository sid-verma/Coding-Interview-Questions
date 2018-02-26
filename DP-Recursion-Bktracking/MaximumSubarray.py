# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# KEY STEP: The current sum would either be the current number or current sum + current number, whichever is greater.
# TC: O(n)
# SC: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(maxSum, currSum)
        return maxSum