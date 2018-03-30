# Implement pow(x, n).
# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000

# Example 2:
# Input: 2.10000, 3
# Output: 9.26100

# KEY STEP: Use FastPow.
# If n is odd, x^n = x^(n/2) * x^(n/2) * x
# If n is even x^n = x^(n/2) * x^(n/2)
# If n is negative FastPow(x, n) = FastPow(1/x, -n)
# If n is 0 => FastPow(x, n) = 1.0
# If n is 1 => Fastpow(x, n) = x

# TC: O(log n) since we are dividing by 2 each time
# SC: o(log n) Use memoization to give back repeating sub problems in O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fastPow(x, n, memoize):
            if n not in memoize:
                if n < 0:
                    return fastPow(1/x, -1*n, memoize)                    
                if n == 0:
                    memoize[n] = 1.0
                if n == 1:
                    memoize[n] = x
                elif n % 2 == 0:
                    memoize[n] = fastPow(x, n/2, memoize) * fastPow(x, n/2, memoize)
                else:
                    memoize[n] = fastPow(x, n/2, memoize) * fastPow(x, n/2, memoize) * x
            return memoize[n]
        return fastPow(x, n, {})