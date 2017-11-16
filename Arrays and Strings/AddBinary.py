# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# Key Step: Recursively add the two numbers from list[:-1].
# If both are 1, then call the function with ((list1, list2), '1') as input and append '0' to the end.
# If both are 0, then we only need to append '0' to the end.
# Else, we need to append '1' to the end.
# TC: O(max(m.n))
# SC: O(1)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'