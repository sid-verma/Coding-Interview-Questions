# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, a solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]

# KEY STEP: 
# - DFS with recursive call
# - Maintain index, current path and result
# - In recursive call, pass new index, append current candidate to path and pass result
# - Base Cases:
#   - If target is negative simply return
#   - If target is 0, return path is correct, so append to result and return

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, index,  path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)
                
        res = []
        dfs(sorted(candidates), target, 0, [], res)
        return res