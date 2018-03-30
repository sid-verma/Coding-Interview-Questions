# There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.
# You can keep inputting the password, the password will automatically be matched against the last n digits entered.
# For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.
# Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.
# Example 1:
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.

# Example 2:
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.

# Note:
# n will be in the range [1, 4].
# k will be in the range [1, 10].
# k^n will be at most 4096.

# KEY STEP: Traverse using DFS to detect Euler Cycle. (De Bruijn Sequences)
# TC: O(n*k^n)
# SC: O(n*k^n)

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                new = node + x
                if new not in visited:
                    visited.add(new)
                    dfs(new[1:])
                    ans.append(x)
        dfs('0'*(n-1))
        return ''.join(ans)+'0'*(n-1)