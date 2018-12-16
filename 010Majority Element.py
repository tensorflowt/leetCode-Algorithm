# -*- coding: utf-8 -*-
#
#  Algorithm function：
#  Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u_nums = set(nums)  #集合（set）是一个无序的不重复元素序列。

        for i in u_nums:
            count = nums.count(i)
            if count > len(nums) // 2:
                return i

if __name__ =='__main__':
    print(Solution().majorityElement([1,2,1,1,3]))