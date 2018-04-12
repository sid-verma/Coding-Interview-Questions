# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".
# Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.
# A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.
# As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.
# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.
# Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.
# Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.
# Given a list of query words, return the number of words that are stretchy. 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1

# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.

# Notes:
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters

# KEY STEP: Run Length Encoding (RLE). Get RLE of S and w in words. The RLE would have a key and freq arr.
# Compare RLE(S) and RLE(w).
# Firstly, keys must be equal.
# Secondly, in loop, if freq(S)[index] < freq(w)[index], then not possible to extend the characters.
# Else, freq(S)[index] must be >= 3 or not possible to extend the characters.
# Count valid words and return count.

# TC: 
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        if len(words) < 1:
            return res
        freq = self.parse(S)
        for w in words:
            # print self.parse(S)
            # print self.parse(w)
            if self.checkEW(freq, self.parse(w)):
                res += 1
        return res
    
    def checkEW(self, wS, wL):
        if len(wS) != len(wL):
            return False
        for i in range(len(wS)):
            if wS[i] < wL[i]:
                return False
            else:
                if wS[i] < 3 and wS[i] != wL[i]:
                    return False
        return True
            
    def parse(self, s):
        arr = [0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if i == len(s)-2:
                    arr[-1] += 2
                    return arr
                else:
                    arr[-1] += 1
            else:
                arr[-1] += 1
                if i == len(s)-2:
                    arr.append(1)
                else:
                    arr.append(0)
        return arr