# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# KEY STEP:
# Perform binary search with a slight modification.
# If lower exceeds array length insert at end of array.
# If lower within array length, but element at lower exceeds target, return lower.
# If higher exceeds array start then insert at 0 index.
# If higher within array start, but element at higher lower than target, return higher+1.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l + h) / 2
            if nums[mid] < target:
                l = mid + 1
                if l < len(nums):
                    if nums[l] > target:
                        return l
                else:
                    return len(nums)
            elif nums[mid] > target:
                h = mid - 1
                if h >= 0:
                    if nums[h] < target:
                        return h + 1
                else:
                    return 0
            else:
                return mid