# Key Step: Using the python reduce function can help.
# reduce [function, [a, b, c]] => function( ... (function(function( function (a, b), c), d), ...)
# Thus we use that with a simple comparison check between two strings
# TC: O(nk)
# SC: O(1)

class Solution(object):
    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        else:
            return reduce(self.lcp, strs)