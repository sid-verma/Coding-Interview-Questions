# Given a collection of distinct numbers, return all possible permutations.
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# KEY STEP: 
# Backtracking over entire array. 
# Similar to GenerateSubset but we only append if size is same as input array.
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        def bt(nums, res, path): 
            if len(path) == len(nums):
                res.append(path)
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                bt(nums, res, path+[nums[i]])
        res = []
        bt(nums, res, [])
        return res