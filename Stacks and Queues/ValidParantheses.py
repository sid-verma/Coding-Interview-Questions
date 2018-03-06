# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# KEY STEP: Use a stack to push elements in. Also maintain a lookup table with key, val as closing, opening
# When we encounter the first closing bracket, check if stack is empty or if popped element isn't matching from the lookup table.
# If the above condition is True then we return False.
# After the look if the stack isn't empty then we return False else True.

# TC: O(n)
# SC: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {"]":"[", ")":"(", "}":"{"}
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == [] or stack.pop() != d[i]:
                    return False
            else:
                return False
        return stack == []