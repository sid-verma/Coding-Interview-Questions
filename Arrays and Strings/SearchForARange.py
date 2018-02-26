# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# KEY STEP: Call binary search twice
# (1) The binary search is designed to return the smallest index at which we can insert a value and still 
# keep the array sorted. This basically returns the starting position
# (2) We call it once on the target value. Then we call it on target+1 
# (3) We subtract -1 from the index of (target+1) to give last position of target

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1, 1]
        def searchPosition(n):
            left, right = 0, len(nums)
            while left < right:
                mid = int((left + right)/2)
                if nums[mid] >= n:
                    right = mid
                else:
                    left = mid+1
            return left
        left = searchPosition(target)
        if target in nums[left:left+1]:
            return [left, searchPosition(target+1)-1]
        else:
            return [-1, 1]