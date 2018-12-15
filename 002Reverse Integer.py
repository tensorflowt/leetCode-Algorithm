# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Given a 32-bit signed integer, reverse digits of an integer.
#  Input: 120
#  Output: 21
#  Input: 123
#  Output: 321
#  Input: -123
#  Output: -321

class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1
        revx = int(str(abs(x))[::-1])  #[::-1]数据翻转
        if x <0:
            revx=revx*sign
        else:
            revx=revx
        if revx < (2**31)-1 and revx >= -2**31:    #针对输出结果做最大、最小值约束。
            return revx
        else:
            return 0


a = Solution()
b = a.reverse(123)
print(b)

