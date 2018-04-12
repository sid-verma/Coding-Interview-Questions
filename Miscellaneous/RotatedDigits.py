# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. 
# Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
# 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
# Now given a positive number N, how many numbers X from 1 to N are good?

# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

# KEY STEP: A good number does not contain 3,4,7 and is madeup of only 0,1,2,5,6,8,9 and contains atleast one of 2,5,6,9 which can be rotated to give a new number.
# TC: O(n log n)
# SC: O (log n)

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for x in range(N+1):
            num = str(x)
            res += all(d not in '347' for d in num) and any(d in '2569' for d in num)
        return res