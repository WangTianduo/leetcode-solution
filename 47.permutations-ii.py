#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(ls, new_num):
            if len(ls) == 0:
                return [[new_num]]
            else:
                ans_set = helper(ls[:-1], ls[-1])
                temp = []
                for item in ans_set:
                    for idx in range(len(item)+1):
                        if idx == 0:
                            if item[0] != new_num:
                                temp.append([new_num]+item)
                        elif idx == len(ls):
                            temp.append(item+[new_num])
                        else:   
                            if item[idx] != new_num: 
                                temp.append(item[:idx]+[new_num]+item[idx:])
                return temp

        if len(nums) == 0:
            return 
        return helper(nums[:-1], nums[-1])

