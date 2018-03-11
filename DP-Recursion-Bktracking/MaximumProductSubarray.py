# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# KEY STEP: DP. Keep track of current max and current min using the DP relation
# Curr{max/min} = max/min(max/min(prevCurr{max/min}*arr[i]), arr[i])
# Update FinalMax = max(FinalMax, Currmax)
# Update prevCurr{max/min} = Curr{max/min}

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        preMaxRightNow = preMinRightNow = maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxRightNow = max(max(preMaxRightNow*nums[i], preMinRightNow*nums[i]), nums[i])
            minRightNow = min(min(preMaxRightNow*nums[i], preMinRightNow*nums[i]), nums[i])
            maxSoFar = max(maxSoFar, maxRightNow)
            preMaxRightNow = maxRightNow
            preMinRightNow = minRightNow
        return maxSoFar