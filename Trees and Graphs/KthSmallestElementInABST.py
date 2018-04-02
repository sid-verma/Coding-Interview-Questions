# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# KEY STEP: InOrder Traversal
# Handle base case for leaf node from helper.
# Recursively call left node.
# Store k as a global variable (initially) and decrement after visiting left subtree.
# Check for k == 0 at root, and update global answer accordingly in helper.
# Recursively call right node from helper.

# TC: O(n)
# SC: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.tIO(root)
        return self.res
        
    def tIO(self, root):
        if not root:
            return
        self.tIO(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.tIO(root.right)