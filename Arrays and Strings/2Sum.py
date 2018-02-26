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
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], nums[i]]
            else:
                d[target-nums[i]] = nums[i]

# This returns the indices of the two numbers that add to the target.

obj = Solution()
print(obj.twoSum([1,4,5,3,5,4,6,3,3,2,4], 7))