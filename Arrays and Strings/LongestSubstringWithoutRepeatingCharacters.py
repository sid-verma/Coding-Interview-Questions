# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# TC: O(n)
# SC: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        d = {}
        longest_substr = 0
        for i in xrange(len(s)):
            #print "At letter: ", i
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                longest_substr = max(longest_substr, i-start + 1)
            d[s[i]] = i
            #print "Start at {}, End at {}".format(start, end)
            #print s[start:end]
        return longest_substr