#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        gap = 1
        result = True
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] >= gap:
                gap = 1
                result = True
            else:
                gap += 1
                result = False
        
        return result

