# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note:
# n and k are non-negative integers.

# KEY STEP: Think using DP.
# If number of colors is 0, then ways = 0
# For fences = 0, the number of ways = 0

# For fences = 1, the number of ways = k

# For fences = 2, there are two possibilities
# - If fences are painted same, then ways_same[2] = k . 1
# - If fences are painted different, then ways_diff[2] = k . (k - 1)
# - Thus, the total no. of ways = k . k

# For fences = i, (where i > 2) we need to think of the same two possibilities,
# - Either the ith fence is painted the same color as (i-1)th fence.
#    - The ways_diff[i-1] would have to be different, else there would be 3 fences painted the same way.
#    - Thus ways_same[i] = ways_diff[i-1]
# - Or ith fence is painted a different color.
#    - It does not matter how ways_[i-1] was painted, since we are painting ith fence with different color.
#    - Thus ways_diff[i] = (ways_same[i-1]+ways_diff[i-1]]) * (k - 1)
# Finally we return ways_same[n] + ways_diff[n]

# TC: O(n)
# SC: O(1)

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = k, k*(k-1)
        for i in range(3, n+1):
            same, diff = diff, (same+diff)*(k-1)
        return same+diff