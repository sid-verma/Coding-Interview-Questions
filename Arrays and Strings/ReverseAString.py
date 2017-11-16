# Reverse a string without using the reverse function.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s)-1
        for i in range(len(s)/2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)