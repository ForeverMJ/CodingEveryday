'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
or equal to target. If there is no such subarray, return 0 instead.

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。



'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res