class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        for i in range(len(s) - 1):
            if convert[s[i]] < convert[s[i + 1]]:
                sum = sum - convert[s[i]]
            else:
                sum = sum + convert[s[i]]

        return sum + convert[s[-1]]

a = Solution()
b = a.romanToInt("MMDC")
print(b)

#说明：
#1.罗马数字的记法：
#a.这种数字采用罗马字母，有四种基本符号：I(1)、X(10)、C(100)、M(1000)和三种辅助符号: V (5)、L(50)、D(500).
#b.相同数字并列时就相加.
#c.不同数字并列时: c-1.小数放在大数的右边就作为加数
#                  c-2.小数放在大数的左边(限于基本符号)，就作为减数。


