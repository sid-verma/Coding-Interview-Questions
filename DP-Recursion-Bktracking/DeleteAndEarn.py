# Given an array nums of integers, you can perform operations on the array. In each operation, you pick any nums[i] and delete it to earn nums[i] points. 
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1. You start with 0 points. 
# Return the maximum number of points you can earn by applying such operations.

# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.

# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# Note:

# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].

# KEY STEP: DP
# We can store the count frequency and traverse Hashmap in a sorted way. For each ith key, we store the prevouis key and do a comparision in the following manner:
# - If the previous key is not consecutive to the current key, then
#   - the best we can do if we select the current key is key*(count[key]) + max(using/avoiding the previous key)
#   - the best we can do if we do not select the current key is max(using/avoiding the previous key)

# - If the previous key is consecutive to the current key, then
#   - the best we can do if we select the current key is key*(count[key]) + avoiding the previous key
#   - the best we can do if we do not select the current key is max(using/avoiding the previous key)

# Finally, we return the max(using/avoiding) after parsing the final key.

# TC: O(NlogN) ~O(N + W) if we use radix sort where W range of allowable values for nums[i]
# SC: O(N), the size of the count dictionary.

import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k-1 != prev:
                avoid, using = max(avoid, using), k*count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*count[k] + avoid
            prev = k
        return max(avoid, using)