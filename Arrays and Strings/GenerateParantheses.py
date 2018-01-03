# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# ["((()))", "(()())", "(())()", "()(())", "()()()"]

# KEY STEP: Backtracking. Define an inside function that appends the resulting string only if the size equals 2N.
# There are two conditions that we need to consider.
# (1) Whether the left '(' bracket can be added. If yes, then we recursively call the backtracing function adding ')'.
# (2) Whether the right ')' bracket can be added. If yes, then we recursviely call the backtracing function adding ')'.
# TC: O(4^n/√n). Each valid sequence has at most n steps during the backtracking procedure.
# SC: O(4^n/√n), as described above, and using O(n)O(n) space to store the sequence.

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S='', left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return ans