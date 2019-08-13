#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

                    nums[i+1:len(nums)] = sorted(nums[i+1:len(nums)])
                    return

        nums.reverse()
                        
                

