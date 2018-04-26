# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# KEY STEP: Traverse using BFS.
# Use two temp lists, one for traversal, and one for storing the values.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [[root]]
        values = [[root.val]]
        while queue != []:
            temp = []
            tempval = []
            nodes = queue.pop(0)
            for n in nodes:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            if temp:
                values.append([x.val for x in temp])
                queue.append(temp)
        return values