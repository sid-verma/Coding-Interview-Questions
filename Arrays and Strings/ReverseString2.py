# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

# KEY STEP: Recursion. There are 3 cases possible
# If remaining string is < k, then reverse it and return
# Else:
#   - If remaining string is in (k, 2k) then reverse upto k and return
#   - If remaining string is > 2k, then reverse upto k for 2k part and call function recursively on remainder beyond 2k.
# Note: Better to create a new swap function for swapping upto index k.

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        l = len(s)
        if l < k:
            s = self.swap(s, len(s))
            return ''.join(s)
        else:
            if l >= k and l < 2*k:
                s = self.swap(s, k)
                return ''.join(s)
            else:
                return ''.join(self.swap(s[:2*k],k)) + self.reverseStr(s[2*k:], k)
            
    def swap(self, s, index):
        for i in range(index/2):
            s[i] , s[index-1-i] = s[index-1-i], s[i]
        return s