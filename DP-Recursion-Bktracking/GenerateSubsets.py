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

# KEY STEP: Recursive DFS.
# - Append path to res in recursive call
# - Iterate from index to array end
# - Recursive call with new element added to path and incremented index

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def bt(nums, res, path, index):
            res.append(path)
            for i in range(index, len(nums)):
                bt(nums, res, path+[nums[i]], i+1)
        res = []
        bt(nums, res, [], 0)
        return res

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# KEY STEP: Same as before with slight modification.
# - Sort the intial array for duplicate check
# - Check nums[i] == nums[i-1]. (Only possible when i > index). If true, then ignore.

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def bt(arr, res, path, index):
            res.append(path)
            for i in range(index, len(arr)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                bt(arr, res, path+[nums[i]], i+1)
        res = []
        bt(nums, res, [], 0)
        return res
