# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# Note: The length of path between two nodes is represented by the number of edges between them.
# Example 1:
# Input:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2

# Example 2:
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# KEY STEP: Recursive call (bit tricky!)
# - At each call we need to return the longer of the next left or right subpaths.
# - When we reach leaf, we should return 0
# - We store the returned value of the recursive call to node.left and node.right in leftPath and rightPath respectively
# - For a parent node, if the left child node is equal in value, the current leftPath (a.k.a leftSubPath) must be leftPath (of node.left) + 1
# - For a parent node, if the right child node is equal in value, the current rightPath (a.k.a rightSubPath) must be rightPath (of node.right) + 1
# - The global value of longestPath can be updated as the maximum of leftSubPath+rightSubPath for a given node
# - Finally we must ensure that the function returns the maximum of either leftSubPath or rightSubPath which is stored in leftPath and rightPath during recursive calls.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def calPath(node):
            if not node: return 0
            
            leftPath = calPath(node.left)
            rightPath = calPath(node.right)
            
            leftSubPath, rightSubPath = 0, 0
            
            if node.left and node.left.val == node.val:
                leftSubPath = leftPath + 1
            if node.right and node.right.val == node.val:
                rightSubPath = rightPath + 1
                
            self.res = max(self.res, leftSubPath + rightSubPath)
            return max(leftSubPath, rightSubPath)
        
        calPath(root)
        return self.res