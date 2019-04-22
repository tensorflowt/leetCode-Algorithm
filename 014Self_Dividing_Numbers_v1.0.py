# encoding: utf-8
#
#  Algorithm function：
#  Input:
#  left = 1, right = 22
#  Output:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#

class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))  #有效地避免循环对象求和问题！

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for num in range(left, right + 1):

            if self.isDividingNumber(num):
                answer.append(num)
        return answer

a = Solution().selfDividingNumbers(0, 22)
print(a)

#说明：
#（1）算法说明：如果一个数字能被它自己的各个位数字整除（比如：24被2整除又被4整除），
# 那么这个数字是一个自除数字，求在[left, right]双闭区间内的所有自除数字。
#（2）算法思路：首先排除输入num中包含0元素的对象，其次采用循环的方法来判断输入对象是否被对象中的各个位的元素所整除。
#注意：
#这里采用sum的方法来对多个整除做判断，感觉不错！