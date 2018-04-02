# In the following, every capital letter represents some hexadecimal digit from 0 to f.
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.
# Note:

# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def getClosestHex(num):
            if num % 17 == 0:
                return hex(num)
            elif num < 17:
                lower = num
                higher = 17 - num
            else:
                lower = num - (num//17)*17
                higher = (num//17+1)*17 - num
                
            if lower > higher:
                return hex(higher+num)
            else:
                return hex(num-lower)
        a = int('0x'+color[1:3], 16)
        b = int('0x'+color[3:5], 16)
        c = int('0x'+color[5:], 16)
        hex_a = getClosestHex(a)
        hex_b = getClosestHex(b)
        hex_c = getClosestHex(c)
        return '#'+ str(hex_a[2:]).zfill(2) + str(hex_b[2:]).zfill(2) + str(hex_c[2:]).zfill(2)