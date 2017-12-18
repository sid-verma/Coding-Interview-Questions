# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 => 1,3,2
# 3,2,1 => 1,2,3
# 1,1,5 => 1,5,1

# Key Step: Start from reverse and proceed till descending order is broken.
# The the element that broke the descending order and swap it with the closest consecutive number in the looped elements till now
# Take the right portion of the margin and sort it in ascending order.

import sys

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums) > 1:
			numbers, temp= [], None
			i = len(nums)-1
			while i > 0:
				numbers.append(nums[i])
				if nums[i-1] < nums[i]:
					break
				i -= 1
			if i != 0:
				# print numbers
				temp = nums[i-1]
				# print temp
				min_index = self.mindiff(nums[i-1], i, nums[i:])
				# print min_index
				nums[i-1] = nums[min_index]
				nums[min_index] = temp
				rem = sorted(nums[i:])
				# print rem
				nums[i:] = rem
			else:
				for i in xrange(len(nums)/2):
					temp = nums[i]
					nums[i] = nums[len(nums)-1-i]
					nums[len(nums)-1-i] = temp
			print nums

	def mindiff(self, target, start, numbers):
		min_diff = sys.maxint
		key = None
		for i in xrange(len(numbers)):
			if numbers[i]-target > 0 and numbers[i]-target < min_diff:
				min_diff = numbers[i]-target
				key = i
		return start+key

test = Solution()
test.nextPermutation([3,2,1])

