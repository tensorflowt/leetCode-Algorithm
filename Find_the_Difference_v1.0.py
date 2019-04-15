# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Input:
#  s="abcd"
#  t="abcde"
#  Output:
#  e

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        have_done = []
        for i in range(0, len(t)):
            if t[i] not in have_done:  #当前字符首次出现
                if t.count(t[i]) == s.count(t[i]):  #字符串t中当前字符出现的次数与字符串s中该字符串出现的次数相同时.
                    pass
                else:
                    return t[i]
                have_done.append(t[i])
            else:
                continue
a = Solution()
b = a.findTheDifference('abcd','aabcd')
print(b)


#说明：
#step1：找到字符串t中的每个字符元素
#step2: 比对字符串t中的每个字符元素出现的次数与字符串s中的对应该字符元素出现的次数
#       若相同，则继续；
#       若不同，则输出当前字符元素。
#注意：这里所需输出元素与元素所在位置无关。
#      例如：s="abcd" t1="abcda" 与 t2="aabcd" 的输出结果是一致的。
