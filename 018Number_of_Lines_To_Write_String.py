# encoding:utf-8
#
#  Algorithm function：
#  Input:
#  widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#  S = "abcdefghijklmnopqrstuvwxyz"
#  Output:
#  [3, 60]
#
class Solution(object):
    def numberOfLines(self, widths, S):
        ABC = "abcdefghijklmnopqrstuvwxyz"
        counter, lines = 0, 1
        _dict = {}

        for i in range(len(widths)):
            _dict[ABC[i]] = widths[i]  #通过字典将输入字符各个元素所占width的值与字符一一对应。

        for i in S:
            counter += _dict[i]
            if counter > 100:
                lines += 1
                counter = _dict[i]  #注意这步很关键，当counter大于100时，将counter置为_dict[i]，直到重新到达100后。
        return [lines, counter]

if __name__ == "__main__":
    widths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    S = "xyzxxx"
    a = Solution().numberOfLines(widths, S)
    print(a)

#算法说明：
#本算法思路关键一步就是通过字典将输入字符各个元素所占width的值与字符一一对应起来。

