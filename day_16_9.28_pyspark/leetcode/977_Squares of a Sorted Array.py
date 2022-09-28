'''
Given an integer array nums sorted in non-decreasing order,
 return an array of the squares of each number sorted
 in non-decreasing order.
给你一个按 非递减顺序 排序的整数数组 nums，
返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
'''

# 双指针算法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j,k = 0,n - 1,n - 1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans



