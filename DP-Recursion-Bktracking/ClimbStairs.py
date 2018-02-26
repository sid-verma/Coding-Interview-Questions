# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Key step: Write out the patterns for n = 1,2,3... and you will see it is a Fibonacci Series.
# Thus you have to simply iterate upto n, and add the previous digit to the current one.
# TC: O(n)
# SC: O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for _ in xrange(n):
            a, b = b, a+b
        return a