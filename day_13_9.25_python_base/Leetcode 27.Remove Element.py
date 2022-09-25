'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        while l<r:
            while(l<r and nums[l]!=val):
                l+=1
            while(l<r and nums[r]==val):
                r-=1
            nums[l], nums[r]=nums[r], nums[l]
        print(nums)
        if nums[l]==val:
            return l
        else:
            return l+1