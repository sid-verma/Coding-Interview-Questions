# Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
# Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
# A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true

# Explanation: 
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.

# Note:
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

# KEY STEP: Use a Binary Search Tree to maintain the start times.

# Create a Node Class
# Have the node object store finish time as well.

# Create a BST search function
# When a new query arrives, recursively search the BST for two conditions
# Either new finish <= old start or newstart >= old finish. When you reach a leaf, you can insert the new node there, so return True.
# Important: You also need to return the node where to insert, so from leaf return True, None and from recursive output return arg1, arg2 if arg2 is not None else, return arg1, currentNode.

# Create an Update BST function.
# This would take the node where to insert and a new Node object with new start, new finish times. Compare start and new start and add new Node to node.left or node.right accordingly.

# TC: O(n^2)
# SC: O(n)

class Node(object):
    def __init__(self, start, end):
        self.s  = start
        self.f = end
        self.left = None
        self.right = None
        
class MyCalendar(object):
    def __init__(self):
        self.root = Node(0, 0)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        res, node = self.checkValidity(self.root, start, end)
        if res:
            newEvent = Node(start, end)
            self.updateCal(node, newEvent)
        return res
                
    def checkValidity(self, node, query_s, query_f):
        if not node:
            return True, None
        if query_s >= node.f:
            res, right = self.checkValidity(node.right, query_s, query_f)
            if res == True:
                if right:
                    return res, right
                return res, node
        elif query_f <= node.s:
            res, left =  self.checkValidity(node.left, query_s, query_f)
            if res == True:
                if left:
                    return res, left
                return res, node
        return False, None
    
    def updateCal(self, node, newEvent):
        if newEvent.s < node.s:
            node.left = newEvent
        else:
            node.right = newEvent

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)