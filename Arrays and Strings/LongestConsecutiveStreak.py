# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
# Given [100, 4, 200, 1, 3, 2],

# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.

# KEY STEP: 
# - O(nlogn) Sort array and parse
# - O(n) Create a set of the array. Start over if num-1 is not in set. Keep increasing streak if num+1 is in set.

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        current_streak = 0
        current_num = 0
        current_set = set(nums)
        for i in nums:
            if i-1 not in current_set:
                current_num = i
                current_streak = 1
            while current_num+1 in current_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak