# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# For example, Given s = “eceba” and k = 2,
# T is "ece" which its length is 3.

# KEY STEP: Use Hashmap to store character frequency count of a sliding window.
# - Keep extending right and updating hashmap and character count
# - If unique characters exceeds k, extend left and keep updating hashmap

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hm = {}
        dc, maxl = 0, 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in hm:
                hm[s[j]] = 1
                dc += 1
                while dc > k:
                    i += 1
                    hm[s[i-1]] -= 1
                    if hm[s[i-1]] == 0:
                        hm.pop(s[i-1], None)
                        dc -= 1
            else:
                hm[s[j]] += 1
            maxl = max(maxl, sum(hm.values()))
            j += 1
        return maxl