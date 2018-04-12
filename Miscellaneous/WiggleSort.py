# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

# KEY STEP: Sort the array and reverse the 2nd half and intermingle with the first.
# TC: O(n log n)
# SC: O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse = i%2)