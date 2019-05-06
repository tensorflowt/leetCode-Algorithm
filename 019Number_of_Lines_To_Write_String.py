class Solution(object):
    def numberOfcurs(self,widths, S):
        lines, counter = 1, 0
        for i in S:
            width = widths[ord(i) - ord('a')]
            lines += 1 if counter + width > 100 else 0
            counter = width if counter + width > 100 else counter + width
        return [lines , counter]


widths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
S = "xyzxxx"
a = Solution().numberOfcurs(widths,S)
print(a)

#算法说明：
#函数ord()返回值是对应的十进制整数。