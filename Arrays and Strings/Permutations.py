# Given a collection of distinct numbers, return all possible permutations.

# KEY STEP:
# This is a one - liner solution so pay attention.
# [n] is the first digit of the permutation
# p is the list returned from recursively calling the permutation function after removing the digit.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return [[n] + p for i, n in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:])] or [[]]
        for i, n in enumerate(nums):
        	for p in self.permute(nums[:i]+nums[i+1:]):
        		return [[n]+p] or [[]]

obj = Solution()
obj.permute([1,2,3])