# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Key Step: Simple iteration over both the lists till the short one expires.
# TC: O(min(m,n))
# SC: O(min(m,n))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2  # This is to ensure the longer list is attached after the shorter one ends.
        return dummy.next