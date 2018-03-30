# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11]

# KEY STEP: Level Order Traversal
# Traverse using DFS and maintain depth count.
# Use hashmap to store values
# After completing traversal, iterate through depth in hashmap and return average.

# TC: O(n) Traversing each node (twice - once in DFS and once in computing average)
# SC: O(n) Storing each node value. Can be optimized if we compute running average to make space O(log n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.levelmap = {}
        def dfs(root, d):
            if not root:
                return
            if d not in self.levelmap:
                self.levelmap[d] = [root.val]
            else:
                self.levelmap[d].append(root.val)
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        print(self.levelmap)
        avglist = []
        dfs(root, 0)
        for key in sorted(self.levelmap.keys()):
            avglist.append(sum(self.levelmap[key])/float(len(self.levelmap[key])))
        return avglist