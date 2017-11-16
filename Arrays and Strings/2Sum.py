# Key Step: If element in dictionary keys then return value, key
# else store the element as the value of key at (target - element).
# TC: O(n)
# SC: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        d = {}
        for i in xrange(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target-nums[i]] = i