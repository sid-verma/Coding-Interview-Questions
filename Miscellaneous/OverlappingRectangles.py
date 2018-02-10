# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.

# KEY STEP:
# (1) Width is the difference between MIN(rightmost x edges) - MAX(leftmost x edges)
# (2) Height is the difference between MIN(topmost y edges) - MAX(bottomost y edges)
# If either are non-positive, there is no overlap.
# Else overlapping area can be calculated.
# Total area covered is area of 2 rectangles - overlapping area.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        ta = abs(C-A)*abs(D-B) + abs(G-E)*abs(H-F)
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        if w <= 0 or h <= 0:
            return ta
        else:
            return ta - w*h