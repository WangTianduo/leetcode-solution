#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        else:
            slow_ptr = 0
            fast_ptr = 0

            while fast_ptr < len(nums):

                if nums[slow_ptr] != val:
                    fast_ptr += 1
                    slow_ptr += 1
                else:
                    while fast_ptr < len(nums) and nums[fast_ptr] == val :
                        fast_ptr += 1
                        length -= 1
                    if fast_ptr < len(nums):
                        temp = nums[fast_ptr]
                        nums[fast_ptr] = nums[slow_ptr]
                        nums[slow_ptr] = temp
                        fast_ptr += 1
                        slow_ptr += 1
            return length


