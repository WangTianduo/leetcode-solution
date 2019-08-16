#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums)-1

        first = last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == 0 or nums[mid-1] < target:
                    first = mid
                    break
                else:
                    right = mid
        if first == -1:
            return [-1, -1]
        left = first
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == len(nums)-1 or nums[mid+1] > target:
                    last = mid
                    break
                else:
                    left = mid+1
        return [first, last]
        

