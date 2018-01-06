# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# KEY STEP: Using DFS. Append tree values during recursive traversal and compare the final lists of both subtrees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.traverseDFSLeft(root.left, []) == self.traverseDFSRight(root.right, [])
        
    def traverseDFSLeft(self, root, arr):
        if not root:
            arr.append(None)
            return
        arr.append(root.val)
        self.traverseDFSLeft(root.left, arr)
        self.traverseDFSLeft(root.right, arr)
        return arr
        
    def traverseDFSRight(self, root, arr):
        if not root:
            arr.append(None)
            return
        arr.append(root.val)
        self.traverseDFSRight(root.right, arr)
        self.traverseDFSRight(root.left, arr)
        return arr