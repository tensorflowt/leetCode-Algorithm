# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Write a program that outputs the string representation of numbers from 1 to n.
#  But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
#  For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range(1,n+1):

            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))
        return list

a = Solution()
b = a.fizzBuzz(15)
print(b)