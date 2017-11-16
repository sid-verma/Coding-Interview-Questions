# Key Step: A neat trick here to use two inline for loops 
# where remainder loops through the aggregate array, and the element looks through the hashed value.
# TC: O(n)
# SC: O(n)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {'1':'',
                   '2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz',
                   '0':''}
        array = [''] if digits else []
        for d in digits:
            array = [rem + elem for elem in letters[d] for rem in array]
        return array