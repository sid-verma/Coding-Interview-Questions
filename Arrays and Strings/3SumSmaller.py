# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

# KEY STEP: Use two pointer method and define a TwoSumSmaller function
# The i marker has range(0, len-2). 
# For each i marker, we call the 2Sum function which seeks two numbers in index range(i+1, len) 
# where arr[p] + arr[q] is less than the new target => target-arr[i]

# TC: O(n^2)
# SC: o(n)

class Solution(object):
    def twoSumSmaller(self, nums, start, target):
        """
        :type nums: List[int]
        :type start: int
        :type target: int
        :rtype: int
        """
        left = start
        right = len(nums)-1
        total = 0
        while left < right:
            if nums[left]+nums[right] < target:
                total += right-left
                left += 1
            else:
                right -= 1
        return total
            
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)-2):
            res += self.twoSumSmaller(nums, i+1, target-nums[i])
        return res