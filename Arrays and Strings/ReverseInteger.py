# Given a 32-bit signed integer, reverse digits of an integer.
# Key Step: Simple approach. Define the limit, extract the sign, and keep reversing.
# TC: O(n)
# SC: O(1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = (2 ** 31)
        y = 0
        if x == 0:
            return y
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        while (x != 0):
            print x, y
            y = 10*y + x%10
            x = x/10
            if (y > limit or y < -1*limit):
                return 0
        return sign*y
        