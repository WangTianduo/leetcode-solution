#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if left == right:
                return left
            elif nums[mid] == target:
                return mid
            elif nums[mid-1] < target < nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

