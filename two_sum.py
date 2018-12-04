# -*- coding: utf-8 -*-
# 
#  Algorithm function：
#  Given nums = [2, 7, 11, 15], target = 9,
#  Because nums[0] + nums[1] = 2 + 7 = 9,
#  return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()

        for index,value in enumerate(nums):  #返回枚举对象
            sub = target - value

            if sub in dic:
                return [dic[sub],index]
            else:
                dic[value] = index

a = Solution()
b = a.twoSum([2,7,11,15],9)
print(b)

#说明：
#[2,7,11,15]
#index   value  sub
#  0      2     7        return  [1,0]
#  1      7     2        return  [0,1]
#  2     11    -2        dic[11]=2
#  3    15     -6        dic[15]=3
