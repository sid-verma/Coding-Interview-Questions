# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice. Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

# KEY STEP: Store left and right index of occurences, and frequencies in dictionaries.
# Then select the max freq keys and out of those, return min subarray length.

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = {}
        freq = {}
        subarrays = []
        
        for i in range(len(nums)):
            if nums[i] not in index:
                index[nums[i]] = [i, i]
                freq[nums[i]] = 1
            else:
                index[nums[i]][1] = i
                freq[nums[i]] += 1

        degree = max(freq.values())

        print(index)
        print(freq)
        print(degree)
        for key in freq.keys():
            subarray_length = index[key][1]-index[key][0]+1
            if freq[key] == degree:
                subarrays.append(subarray_length)

        return min(subarrays)