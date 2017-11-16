# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in xrange(1, n+1):
            if i%3 == 0:
                if i % 5 == 0:
                    l.append("FizzBuzz")
                else:
                    l.append("Fizz")
            elif i%5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l