# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
# Also given an integer k, you need to output in the last day when there exists two flowers in the status of blooming, while there are k flowers between them that are not blooming.
# If there isn't such day, output -1.

# Example 1:
# Input: 
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.

# Example 2:
# Input: 
# flowers: [1,2,3]
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        ans = float('inf')
        days = [0]*len(flowers)

        for day, location in enumerate(flowers, 1):
        	days[location-1] = day

        left, right = 0, k + 1

        while right < len(days):
        	for i in range(left + 1, right):
        		if days[i] < days[left] or days[i] < days[right]:
        			left, right = i, i + k + 1
        			break
        	else:
        		ans = min(ans, max(days[left], days[right]))
        		left, right = right, right + k + 1
        return ans if ans < float('inf') else -1