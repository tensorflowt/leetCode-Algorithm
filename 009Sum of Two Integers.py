# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # c = a + b
        # return c
        list = [a,b]
        return sum(list)   #sum针对列表、元组、集合计算

if __name__ == '__main__':
    print(Solution().getSum(-2,3))
