#
# @lc app=leetcode id=1144 lang=python3
#
# [1144] Decrease Elements To Make Array Zigzag
#
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        odd_min = 0
        even_min = 0
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                if i == 0:
                    if nums[i] >= nums[i+1]:
                        odd_min += nums[i] - nums[i+1] + 1
                elif i == len(nums)-1:
                    if nums[i] >= nums[i-1]:
                        odd_min += nums[i] - nums[i-1] + 1
                else:
                    min_neighbor = min(nums[i-1], nums[i+1])
                    if nums[i] >= min_neighbor:
                        odd_min += nums[i] - min_neighbor + 1
            else:
                if i == len(nums)-1:
                    if nums[i] >= nums[i-1]:
                        even_min += nums[i] - nums[i-1] + 1
                else:
                    min_neighbor = min(nums[i-1], nums[i+1])
                    if nums[i] >= min_neighbor:
                        even_min += nums[i] - min_neighbor + 1
        return min(odd_min, even_min)
        

