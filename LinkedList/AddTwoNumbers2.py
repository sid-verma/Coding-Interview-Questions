# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# KEY STEP: Use 2 stacks. Push the linkedlists into them and pop and add.
# You can store the result in an array and parse throught it while creating the final LinkedList.
# TC: O(m+n)
# SC: O(m+n)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []

        # Pushing Linked Lists into 2 stacks
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        nums = []
        prev = 0
        while s1 or s2:
            if s1 == [] or s2 == []:
                if s1:
                    temp = s1.pop() # If s2 is empty
                else:
                    temp = s2.pop() # If s1 is empty
            else:
                temp = s1.pop() + s2.pop() # If none are empty

            carry, res = divmod(prev+temp, 10)
            nums.append(res)
            prev = carry

        if prev:	# To check last carry
            nums.append(prev)
        
        res = ListNode(0)
        node = res
        for i in range(len(nums)):
            node.next = ListNode(nums[len(nums)-i-1])
            node = node.next
        return res.next