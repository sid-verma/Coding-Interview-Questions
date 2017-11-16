# Key Step:
# To solve this problem, we need to understand "What is the use of median". 
# In statistics, the median is used for dividing a set into two equal length subsets, that one subset is always greater than the other.
# If we understand the use of median for dividing, we are very close to the answer.
# First let's cut A into two parts at a random position i:
#       left_A             |        right_A
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]

# Since A has m elements, so there are m+1 kinds of cutting( i = 0 ~ m ). And we know: len(left_A) = i, len(right_A) = m - i .
# Note: when i = 0 , left_A is empty, and when i = m , right_A is empty.
# With the same way, cut B into two parts at a random position j:
#       left_B             |        right_B
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

# Put left_A and left_B into one set, and put right_A and right_B into another set. Let's name them left_part and right_part :
#       left_part          |        right_part
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

# If we can ensure:
# 1) len(left_part) == len(right_part)
# 2) max(left_part) <= min(right_part)
# then we divide all elements in {A, B} into two parts with equal length, and one part is always greater than the other.
# Then median = (max(left_part) + min(right_part))/2.

# TC: O(log(min(m,n)))
# SC: O(1)

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        imin, imax, hl = 0, m, (m + n + 1)/2
        while imin <= imax:
            i = (imin + imax)/2
            j = hl - i
            if i < m and A[i] < B[j-1]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: # [| . . . ], [. . . . . | . . . .]
                    max_left = B[j-1]
                if j == 0: # [. . . . . | . . . .], [| . . . .]
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return max_left
                if i == m: # [. . . |], [ . . . . | . . . . ]
                    min_right = B[j]
                elif j == n: # [ . . . . | . . . . ], [. . . |] 
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                return (max_left + min_right) / 2