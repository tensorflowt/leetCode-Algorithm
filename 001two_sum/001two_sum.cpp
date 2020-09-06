/*
Data：2020-09-06 19：39
Author: william
Function:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数并返回他们的数组下标。
你可以假设每种输入只会对应一个答案(这点很重要)。
但是，数组中同一个元素不能使用两遍。
Algorithm thought：
把给定的整数数组nums看作是一个集合，然后在这个集合里随机取2个元素，与顺序无关，那么就有C42种取法，即也就是这里的嵌套循环.
之后再加一个条件判断即可.
*/

#include <string.h>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		int i, j;
		for (i = 0; i < nums.size() - 1; i++)
		{
			for (j = i + 1; j < nums.size(); j++)
			{
				if (nums[i] + nums[j] == target)
				{
					return { i,j };
				}
			}
		}
		return { i,j };
	};
};

int main(void)
{
	Solution Test;
	vector<int> nums = { 2, 7, 11, 15 };
	vector<int> result;
	int target = 17;
	result = Test.twoSum(nums,target);
	int i;
	for (i = 0; i < result.size(); i++)
	{
		cout << "第" << i << "个元素对应的下标为:" << result[i] << "\n";
		cout << "第" << i << "个元素为:" << nums[result[i]] << "\n";
	};
	system("pause");

}