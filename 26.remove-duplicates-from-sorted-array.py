#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        pos = 1
        old_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != old_num:
                nums[pos] = nums[i]
                pos += 1
                old_num = nums[i]
        return len(nums[:pos])
