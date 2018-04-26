# Given a binary tree
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Note:
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.

# Example:
# Given the following binary tree,
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# After calling your function, the tree should look like:
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL

# KEY STEP: Level Order Traversal using BFS.
# For each level, during iteration, assign the next node for i = 0, .., l-2. For i = l-1, the node is going to stay None by default.
# TC: O(n)
# SC: O(1)

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue =[[root]]
        while queue != []:
            temp = []
            nodes = queue.pop(0)
            for i in range(len(nodes)):
                if i < len(nodes)-1:
                    nodes[i].next = nodes[i+1]
                if nodes[i].left:
                    temp.append(nodes[i].left)
                if nodes[i].right:
                    temp.append(nodes[i].right)
            if temp:
                queue.append(temp)