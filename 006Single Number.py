# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Given a non-empty array of integers, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res = res^i  #位异或
        return res

a = Solution().singleNumber([1,1,2])
print(a)

#说明：
#位异或属于python中位运算符中的一种，位运算符只能适用于整数，其运算规则为：
#首先把整数转换为二进制表示形式，按最低位对齐，短的高位补0，然后进行位运算，最后把得到的二进制转换为十进制数。

#[1，1，2]
#1 - 01
#1 - 01
#计算异或得到：00
#2 - 10
#计算异或得到：10
#转为十进制：2

