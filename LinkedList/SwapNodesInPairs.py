# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space. 
# You may not modify the values in the list, only nodes itself can be changed.

# KEY STEP:
# define pre as the previous node. Have pre.next as head.
# a and b represent the current and next nodes in the LinkedList.
# Perform the following swap. Example is shown below.

#    PRE.NEXT*
#       A           A.NEXT
#                     B             B.NEXT
#       1     ->      2       ->      3       ->      4       ->       5  => PRE.NEXT = B

#                   PRE.NEXT*
#       A           A.NEXT
#                     B             B.NEXT
#       1     ->      2       ->      3       ->      4       ->       5  => B.NEXT = A

#                   PRE.NEXT*
#       A           A.NEXT
#       B.NEXT        B             B.NEXT(*old)
#       1     <-      2               3       ->      4       ->       5  => A.NEXT = B.NEXT (* old)

#       PRE                         PRE.NEXT*
#       A                           A.NEXT
#       B.NEXT        B  
#       -------------------------------
#       |                             |
#                                     v
#       1     <-      2               3       ->      4       ->       5  => PRE = A

#       2      ->     1       ->      3       ->      4       ->       5    

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = self
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next