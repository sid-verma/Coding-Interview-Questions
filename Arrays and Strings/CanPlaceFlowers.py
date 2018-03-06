# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False

# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

# KEY STEP: Check whether it is legal to put a flower. If the f[i] = 0 and f[i+1] = 0 and f[i-1] = 0, then we can.
# However, for i = 0 and i = last, we are only concerned with f[i+1] = 0 and f[i-1] = 0 respectively.
# Thus, we can combine the condition as f[i] = 0 AND (i = 0 OR f[i-1] = 0) AND (i = last OR f[i+1] = 0)

# TC: O(n)
# SC: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False