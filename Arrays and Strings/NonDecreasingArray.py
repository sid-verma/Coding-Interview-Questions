# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# KEY STEP: 

# Intuition ===>
# Consider all indices p for which A[p] > A[p+1]. If there are zero, the answer is True. 
# If there are 2 or more, the answer is False, as more than one element of the array must be changed for A to be monotone increasing.
# At the problem index p, we only care about the surrounding elements. 
# Thus, immediately the problem is reduced to a very small size that can be analyzed by casework.

# Algorithm ===>
# As before, let p be the unique problem index for which A[p] > A[p+1].
# If this is not unique or doesn't exist, the answer is False or True respectively. We analyze the following cases:

# If p = 0, then we could make the array good by setting A[p] = A[p+1].
# If p = len(A) - 2, then we could make the array good by setting A[p+1] = A[p].

# Otherwise, A[p-1], A[p], A[p+1], A[p+2] all exist, and:

# We could change A[p] to be between A[p-1] and A[p+1] if possible, or;
# We could change A[p+1] to be between A[p] and A[p+2] if possible.

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if flag is not None:
                    return False
                flag = i
        return flag == None or flag == 0 or flag == len(nums)-2 or nums[flag-1] <= nums[flag+1] or nums[flag] <= nums[flag+2]