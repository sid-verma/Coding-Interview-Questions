# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.append(upper+1)
        start = lower-1
        for i in range(len(nums)):
            if nums[i] == start+2:
                #insert just the missing number
                res.append(str(nums[i]-1))
            elif nums[i] > start+2:
                #insert the missingrange
                res.append(str(start+1)+'->'+str(nums[i]-1))
            start = nums[i]
        return res