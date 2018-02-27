# Given a sorted (increasing order) array with unique integer elements, 
# write an algorithm to create a binary search tree with minimal height.

# KEY STEP:
# 1. Assign the middle element as the node value by providing start and end indices of array
# 2. Recursively call function for creating left subtree with reduced indices.
# 3. Recusrively call function for creating right subtree with reduced indices.
# 4. The base case is when end index < start index. Return null for that case.

class Solution():
	def createMinimalBST(self, arr):
		return createMinimalBST(remaining_array, start, end)

	def createMinimanBST(arr, start, end):
		if end < start:
			return None
		mid = (start + end)/2
		n = TreeNode(arr[mid])
		n.left = self.createMinimalBST(arr, start, mid-1)
		n.right = self.createMinimalBST(arr, mid+1, end)
		return n
