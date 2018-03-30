# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.

# KEY STEP: DFS. 
# Since the diameter can be a subtree, we calculate the global diameter at each node by comparing current value to left_path + right_path + 1.
# But from a single node, we want to return only the longest path to the parent node, so that this becomes either the left_path or right_path for the parent node.
# Hence we finally return max(left_path, right_path) + 1.
# The final answer will be returned value -1 since the path = no. of edges = no. of nodes -1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def getDiameter(node):
            if not node:
                return 0
            left = getDiameter(node.left)
            right = getDiameter(node.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right) + 1
        getDiameter(root)
        return self.ans-1