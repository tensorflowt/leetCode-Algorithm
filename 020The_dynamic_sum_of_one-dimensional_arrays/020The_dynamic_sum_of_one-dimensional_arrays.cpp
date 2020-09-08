/*
Data：2020-09-08
Author: william
Function:
给你一个数组 nums 。
数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
Algorithm thought：
说明：
[1,2,3,4]
i=0
nums[1]=nums[1]+nums[0]=2+1=3
nums[2]=nums[2]+nums[1]=3+3=6
nums[3]=nums[3]+nums[2]=4+6=10
[1,3,6,10]
*/
#include <string.h>
#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
	public:
		vector<int> runningSum(vector<int>& nums)
		{
			int size = nums.size();
			for (int i = 1; i < size; i++)
				nums[i] += nums[i - 1];
			return nums;
		}
};

int main(void)
{
	Solution Test;
	vector<int> nums = { 1,2,3,4 };
	vector<int> result;

	result = Test.runningSum(nums);

	int i;
	for (i = 0; i < result.size(); i++)
		std::cout << result[i] << " "; 
	std::cout << std::endl;

	system("pause");
}