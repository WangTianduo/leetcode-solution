#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        memo = dict()
        def helper(n, k, memo):
            if (n,k) in memo.keys():
                return memo[(n,k)]
            elif n == 1:
                memo[(n, k)] = [[1]]
                return [[1]]
            elif k == 1:
                memo[(n, k)] = [[x] for x in range(1, n+1)]
                return [[x] for x in range(1, n+1)]
            elif n == k:
                memo[(n, k)] = [[x for x in range(1, n+1)]]
                return [[x for x in range(1, n+1)]]
            else:
                result = list()
                result = helper(n-1, k, memo)

                temp = helper(n-1, k-1, memo)

                for item in temp:
                    result.append(item+[n])
                memo[(n, k)] = result
                return result
        
        return helper(n, k, memo)


