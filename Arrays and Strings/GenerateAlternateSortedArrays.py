# Given two sorted arrays A and B, generate all possible arrays such that first element is taken from A then from B then from A and so on in increasing order till the arrays exhausted. The generated arrays should end with an element from B.

# For Example 
# A = {10, 15, 25}
# B = {1, 5, 20, 30}

# The resulting arrays are:
#   10 20
#   10 20 25 30
#   10 30
#   15 20
#   15 20 25 30
#   15 30
#   25 30

# KEY STEP: Think using Recursion. But you need to handle the first case.

class Solution(object):
	"""docstring for Solution"""
	def genSortedArrays(self, A, B):
		C = []
		return self.generateUtil(A, B, C, 0, 0, len(A), len(B), 0, True)

	def generateUtil(self, A, B, C, i, j, m, n, l, flag):
		# If we have to pick from A
		if flag:
			if l != 0:
				print(C)
			for k in range(i, m):
				# This is for the beginning case only
				if l == 0:
					C.append(A[k])
					self.generateUtil(A, B, C, k+1, j, m, n, l, not(flag))
				else:
					if A[k] > C[l]:
						C.append(A[k])
						self.generateUtil(A, B, C, k+1, j, m, n, l+1, not(flag))

		#  If we have to pick from B
		else:
			for k in range(j, n):
				if B[k] > C[l]:
					C.append(B[k])
					self.generateUtil(A, B, C, i, k+1, m, n, l+1,  not(flag))

A = [10, 15, 25]
B = [1, 5, 20, 30]
obj = Solution()
obj.genSortedArrays(A, B)