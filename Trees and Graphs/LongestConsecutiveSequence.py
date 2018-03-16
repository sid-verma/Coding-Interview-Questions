# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
# The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# KEY STEP: Recursive call to left and right subtree with parent node val.
# - Check if consecutive, then increment gobal res by 1 and take max of (left call, right call)
# - If not consecutive, then set global res to 1 and take max of (left call, right call, current global res)

# TC: O(n)
# SC: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def lcp(root, prev, res):
            if not root:
                return res
            else:
                if root.val - prev == 1:
                    return max(lcp(root.left, root.val, res+1), lcp(root.right, root.val, res+1))
                else:
                    return max(res, lcp(root.left, root.val, 1), lcp(root.right, root.val, 1))
        return lcp(root, root.val-1,0)