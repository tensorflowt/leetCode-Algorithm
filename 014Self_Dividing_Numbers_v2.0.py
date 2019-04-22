# encoding: utf-8
#
#  Algorithm function：
#  Input:
#  left = 1, right = 22
#  Output:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#

class Solution:
    def isSDN(self, n):
        m = n
        while n > 0:
            temp = n % 10
            if temp == 0:   #如果temp被10整除（说明是10的倍数，肯定包含0但大于0（排除））
                return False
            if m % temp != 0:  #如果m不被temp所整除（说明该num不被非首位元素整除（排除））
                return False
            n //= 10  #求商(例如：对于251，分别为251，25，2.也就是说理论上需要做3次判断)
        return True

    def selfDividingNumbers(self, left: int, right: int):
        res = []
        for i in range(left, right + 1):
            if self.isSDN(i):
                res.append(i)
        return res

a = Solution().selfDividingNumbers(1,251)
print(a)

#说明：
#（1）算法说明：如果一个数字能被它自己的各个位数字整除（比如：24被2整除又被4整除），
# 那么这个数字是一个自除数字，求在[left, right]双闭区间内的所有自除数字。

