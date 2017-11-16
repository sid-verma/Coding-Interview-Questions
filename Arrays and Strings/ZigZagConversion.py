# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

# Key Step: The main idea is to view the grid horizontally. 
# So we append letters to a window of size numRows and we keep adding till we hit the right end.
# Then we reverse and keep adding till we hit the left end.
# Finally we 
#   1   2   3   .   .   .   numRows-1
#   E   R   T   F   H   B   X -> Keep moving right till end
#   .   .   .   .   .   C   . <- Hit end start shifting left
#   .   .   .   .   N   .   . <- Shift left
#   .   .   .   S   .   .   . <- Shift left
#   .   .   Y   .   .   .   . <- Shift left
#   .   M   .   .   .   .   . <- Shift left
#   J   G   B   N   H   U   O -> Keep moving right till end
#   .   .   .   .   .   C   . <- Hit end start shifting left
#   .   .   .   .   P   .   . <- Shift left
#   .   .   .   C   .   .   . <- Shift left
#   .   .   K   .   .   .   . <- Shift left
#   .   G   .   .   .   .   . <- Shift left
#   X   Z   G   W   B   M   N -> Keep moving right till end
# and so on...

# TC: O(n)
# SC: O(n)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        arr = ['']*(numRows)
        index,step = 0,1
        for i in s:
            arr[index] += i
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return "".join(arr)