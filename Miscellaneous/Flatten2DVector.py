# Implement an iterator to flatten a 2d vector.
# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.pos = 0
        self.vec = 0

    def next(self):
        """
        :rtype: int
        """
        elem = self.vec2d[self.vec][self.pos]
        self.pos += 1
        return elem
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.vec < len(self.vec2d):
            if self.pos < len(self.vec2d[self.vec]):
                return True
            self.pos = 0
            self.vec += 1
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())