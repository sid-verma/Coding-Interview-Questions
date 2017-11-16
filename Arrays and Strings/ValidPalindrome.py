class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        if s == "":
            return True
        else:
            for i in s:
                if i.isalnum():
                    l.append(i.lower())
        return l == l[::-1]