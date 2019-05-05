# encoding:utf-8
class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y  #按位异或运算符：当两对应的二进位相异时，结果为1
        count = 0
        while xor > 0:  #当且仅当x与y所对应的二进制的数值存在异位时，才做如下判断。
            if xor & 1:  #结果为非零时成立
                count += 1
            xor = xor >> 1  #右移动运算符（即对其二进制的数据每次更新时去掉右数第一个元素）
        return count

if __name__ =="__main__":
    a = Solution().hammingDistance(4,10)
    print(a)

#算法思路
#首先通过位异或符（^）计算出两个整数的差异xor；
#其次通过将差异xor与整数1做位与运算符（&），即：当其结果为非0时，差异项数（count）加一。
#之后，通过右移动运算符（>>）将xor按位依次与整数1做比较，直至xor小于0时，循环结束。

#小结：其实整个算法最关键的是：通过位异或符（^）计算出两者差异xor后如何确定差异个数？

#关于Hamming Distance的介绍：https://en.wikipedia.org/wiki/Hamming_distance
