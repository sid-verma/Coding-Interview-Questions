# Given a binary tree, return the inorder traversal of its nodes' values.
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?


# Trivial Recursive Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def iot(self, root, nodes):
        if not root:
            return
        self.iot(root.left, nodes)
        nodes.append(root.val)
        self.iot(root.right, nodes)
        return
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.nodes = []
        self.iot(root, self.nodes)
        return self.nodes

# Not so Trivial, Iterative Solution