# -*- coding: utf-8 -*-
#  Algorithm function：
#  Write a function to find the longest common prefix string amongst an array of strings.
#  If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != strs[0][i]: 
                    return res

            res += strs[0][i]
        return res


b = ["flower","flow","flight"]
a = Solution().longestCommonPrefix(b)
print(a)


#说明：
#1.算法功能：
#["a","a","b"]  返回 ""，因为三个字符串没有公共前缀；
#["a","a"]  返回 "a" 因为它是两个字符串的公共前缀；
#["abcd","abc"]  返回 "abc"；
#["ac","ac","a","a"]  返回 "a" 。

#2.算法思路：
# 从任意一个字符串开始，扫描该字符串，依次检查其他字符串的同一位置是否是一样的字符，当遇到不一样时则返回当前得到的前缀。

#3.代码说明：
#   if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
#       return res
#该条件好比一个故障检测器，当出现符合故障的条件时，机器停止运行，并返回停止前的最近一次结果。
#故障条件：当初始的字符串长度大于其他字符串长度时或初始的字符串的当前位置的字符与其他字符串同一个位置下的当前位置的字符不同时，