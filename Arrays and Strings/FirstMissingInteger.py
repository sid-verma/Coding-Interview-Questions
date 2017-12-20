# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space.

# KEY STEP:
# 1st loop - Remove elements that are negative and > array length.
# 2nd loop - Hash elements in place by % len(arr) += len(arr)
# 3rd loop - Elements that / len(arr) == 0 will be the 1st missing integer.

# TC: O(n)
# SC: O(1)

class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.append(0)
		n = len(nums)
		for i in range(len(nums)): 
			if nums[i]<0 or nums[i]>=n:
				nums[i]=0
		for i in range(len(nums)):
			nums[nums[i]%n]+=n
		for i in range(1,len(nums)):
			if nums[i]/n==0:
				return i
		return n