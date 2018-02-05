# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. 
# You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

# KEY STEP:
# There is a clear recursion available: the final cost f[i] to climb the staircase from some step i is f[i] = cost[i] + min(f[i+1], f[i+2]). 
# This motivates dynamic programming.

# Algorithm
# Let's evaluate f backwards in order. That way, when we are deciding what f[i] will be, we've already figured out f[i+1] and f[i+2].
# We can do even better than that. At the i-th step, let f1, f2 be the old value of f[i+1], f[i+2], and update them to be the new values f[i], f[i+1].
#We keep these updated as we iterate through i backwards. At the end, we want min(f1, f2).

# TC: O(n)
# SC: O(1)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for i in reversed(cost):
            f1, f2 = i + min(f1, f2), f1
        return min(f1, f2)