# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?

# KEY STEP:
# (1) Dynamic Programming - O(n^2)
#    - Maintain initial table of array size with each element = 1 (since LIS of size 1 is 1)
#    - Iterate i from (1 ... n-1). Iterate j from (1 ... i)
#    - LIS[i] = max(LIS[i], LIS[j]+1)
#    - Return the max LIS

# (2) DP with Binary Search - O(nlogn)

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        lis = [1]*l
        lis_len = 0
        for i in range(1, l):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], (lis[j]+1))
            # print(lis[i])
        for i in lis:
            if i > lis_len:
                lis_len = i
        return lis_len

# Solution: DP + Binary Search O(nlogn)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0]*len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i + j)/2)
                if tails[m] < x:
                    i = m+1
                else:
                    j = m
            tails[i] = x
            size = max(i+1, size)
        return size