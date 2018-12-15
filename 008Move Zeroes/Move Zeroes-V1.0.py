# -*- coding: utf-8 -*-
#  Algorithm function：
#  Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            # print(num)
            if num != 0:
                nums[i] = num
                i += 1
        print(i)
        for j in range(i, len(nums)):  #此处i为第一个非0元素所对象的索引号
            nums[j] = 0
        return nums

print(Solution().moveZeroes([1,2,3,0,4]))

#说明：
#先将所有的非零元素移动到前面，再将剩下的元素全都置为0。