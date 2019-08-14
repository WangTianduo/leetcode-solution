#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 or n == 1:
            return 1
        else:
            m -= 1
            n -= 1
            total = m + n
            
            if m > n:
                small = n
                large = m
            else:
                small = m
                large = n
            upper = 1
            down = 1
            for i in range(small):
                upper *= total - i
                down *= small - i
            
            return upper // down
            
        # below is the direct dp algorithm
        # def check_block(map_m, map_n, x, y):
        #     if map_m == x + 1 or map_n == y + 1:
        #         return True
        #     else:
        #         return False

        # start_point = [0, 0]

        # memo = dict()

        # def helper(start_point):
        #     if (start_point[0], start_point[1]) in memo:
        #         return memo[(start_point[0], start_point[1])]
        #     elif check_block(m, n, start_point[0], start_point[1]):
        #         memo[(start_point[0], start_point[1])] = 1
        #         return 1
        #     else:
        #         memo[(start_point[0], start_point[1])] = helper([start_point[0]+1, start_point[1]]) + helper([start_point[0], start_point[1]+1])
        
        #         return memo[(start_point[0], start_point[1])]
        
        # return helper([0, 0])

