# Given a collection of numbers (not distinct), return all possible permutations.

# KEY STEP:
# Same as permutations. However we need to add an extra line to remove duplicate lists from the answer.
# [n] is the first digit of the permutation
# p is the list returned from recursively calling the permutation function after removing the digit.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(x) for x in set(tuple(y) for y in self.permute(nums))]
        
    def permute(self, nums):
        return [[n] + p for i, n in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:]) or [[]]]