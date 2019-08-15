#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(target, avail, idx, path, res):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            else:
                for i in range(idx, len(candidates)):
                    if i>idx and avail[i] == avail[i-1]:
                        continue
                    else:
                        dfs(target-avail[i], avail, i+1, path+[avail[i]], res)

        res = []
        candidates.sort()
        dfs(target, candidates, 0, [], res)
        return res

