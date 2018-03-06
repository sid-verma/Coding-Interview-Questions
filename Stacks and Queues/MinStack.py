# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# KEY STEP: Either store each element as (element, currentMin) tuple OR use a send stack to store currentMin.

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currMin = self.getMin()
        if x <= currMin or currMin == None:
            self.minStack.append(x)
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        if self.stack != []:
            if self.stack[-1] == self.getMin():
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack != []:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack != []:
            return self.minStack[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()