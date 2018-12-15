# -*- coding: utf-8 -*-
#  Algorithm function：
#  Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] ==0:
                num_zeroes = num_zeroes+1
            else:
                t = nums[i]
                nums[i] = 0
                nums[i - num_zeroes] = t   #将当前非零元素往零元素的前面移动，有多少个0元素，就移动多少个索引号。


        return nums

print(Solution().moveZeroes([1,2,0,0,3,0]))

