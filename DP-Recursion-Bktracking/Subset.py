# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# KEY STEP: Backtracking. Use DFS to recursively add to path.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, sorted(nums), [], 0)
        return res
    
    def dfs(self, res, nums, subset, start):
        res.append(subset)
        for i in xrange(start, len(nums)):
            self.dfs(res, nums, subset+[nums[i]], i+1)