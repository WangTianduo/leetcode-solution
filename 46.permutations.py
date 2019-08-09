#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ls, new_num):
            if len(ls) == 0:
                return [[new_num]]
            else:
                ans_set = helper(ls[:-1], ls[-1])
                temp = []
                for item in ans_set:
                    for idx in range(len(item)+1):
                        if idx == 0:
                            temp.append([new_num]+item)
                        elif idx == len(ls):
                            temp.append(item+[new_num])
                        else:    
                            temp.append(item[:idx]+[new_num]+item[idx:])
                return temp

        if len(nums) == 0:
            return 
        return helper(nums[:-1], nums[-1])

