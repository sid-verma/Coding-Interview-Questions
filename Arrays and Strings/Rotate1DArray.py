# Key Step: Reverse upto the length-k part.
#           Reverse the remaining part. 
#           Then reverse the entire array.
# TC: O(n) parses through the array thrice
# SC: O(1) in place
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        while k > length:
            k = k%length
        nums[:length-k] = self.reverse(nums[:length-k])
        nums[length-k:] = self.reverse(nums[length-k:])
        for i in xrange(len(nums)/2):
            nums[i], nums[length-1-i] = nums[length-1-i], nums[i]
            
    def reverse(self, a):
        return a[::-1]