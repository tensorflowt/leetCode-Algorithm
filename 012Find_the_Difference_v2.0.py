class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:   # 获取两个字符串中的所有字符元素
            ans = ans^ord(c)
        return chr(ans)

a = Solution()
b = a.findTheDifference('abab','ababa')
print(b)


# 说明:
# 函数ord():表示对字符进行编码,返回对应的十进制整数
# 位运算符:通过对运算对象进行二进制转换,然后按最低位对齐，短的高位补0，然后进行位运算，最后把得到的二进制转换为十进制数。
# 进一步了解可参考博文：https://blog.csdn.net/william_hehe/article/details/85005630
