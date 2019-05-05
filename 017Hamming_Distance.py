# encoding:utf-8
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

if __name__ == "__main__":
    a = Solution().hammingDistance(4,10)
    print(a)


#算法说明：
#首先通过位异或符（^）计算出两个整数的差异xor；
#其次，确定差异xor中的差异个数。

#内置函数count() 方法用于统计字符串里某个字符出现的次数。
#内置函数bin（）转换一个整数x为二进制的字符串表示。