# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# For example, the numbers "69", "88", and "818" are all strobogrammatic.

# KEY STEP: Define sets for 0,1,8 and 6,9. Check by making cases and for palindromic sequences.

# TC: O(n)
# SC: O(1)

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sgm = set(['0', '1', '8'])
        revsgm = set(['6','9'])
        i, j = 0, len(num)-1
        while i < j:
            if num[i] != num[j]:
                if num[i] not in revsgm or num[j] not in revsgm:
                    return False
            else:
                if num[i] not in sgm or num[j] not in sgm:
                    return False
            i += 1
            j -= 1
        if len(num)%2 != 0:
            print(num[i])
            if num[i] not in sgm:
                return False
        return True