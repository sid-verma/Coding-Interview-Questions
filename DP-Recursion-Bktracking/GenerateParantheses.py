# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# KEY STEP: Backtracking with DFS
# - Backtrack for left < n
# - Backtrack for right < left
# - Append when left + right == 2n
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def bt(num, left, right, res, path):
            if left + right == 2*n:
                res.append(path)
            if left < n:
                bt(num, left+1, right, res, path+"(")
            if right < left:
                bt(num, left, right+1, res, path+")")
        bt(n, 0, 0, res, "")
        return res