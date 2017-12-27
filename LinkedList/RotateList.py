# Given a list, rotate the list to the right by k places, where k is non-negative.
# Example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 1:
            return head
        node, count = head, 0
        while node.next:
            node = node.next
            count += 1
        while k > count+1:
            k = k%(count+1)
        node.next = head
        for i in xrange(0, count-k+1):
            node = node.next
        dummy = node.next
        node.next = None
        return dummy