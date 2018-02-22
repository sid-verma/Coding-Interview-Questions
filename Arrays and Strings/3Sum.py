# Key Step: [.  .   .   .   .   .]
#            ^  ^               ^
#            i start =>      <= end
# Sort the array.
# Keep incrementing start and decrementing end and checking for values if they add upto 0.
# If value < 0, then increment start till it attains a new value.
# If value > 0, then decrement end till it attains a new value.
# Use a dicitionary to avoid repeated triplets.
# TC: O(n^2)
# SC: O(n)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # This is to ensure that the numbers are not the same
                continue
            start, end = i+1, len(nums)-1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < 0:
                    start +=1 # Moving start up
                elif s > 0:
                    end -= 1 # Moving end down
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start+1]: # To check whether upcoming numbers are the same, then ignore
                        start += 1
                    while start < end and nums[end] == nums[end-1]: # To check whether upcoming numbers are the same, then ignore
                        end -= 1
                    start += 1; end -= 1
        return res

obj = Solution()
print(obj.threeSum([1,2,7,-1,4,0,-3,3,5,4,-3]))