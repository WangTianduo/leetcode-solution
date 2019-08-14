#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        
        height = len(obstacleGrid)
        # if only 1d
        width = len(obstacleGrid[0])
        total_layer = height + width - 2

        dp = [[0 for _ in range(width)] for _ in range(height)]
        dp[0][0] = 1
        last_avail = [(0, 0)]
        avail = []
        layer = 0
        while layer <= total_layer:
            # layer: int; start from 1
            avail = []
            layer += 1
            for w in range(layer+1):
                h = layer - w
                if h < height and w < width and obstacleGrid[h][w] == 0:
                    avail.append([h, w])
            for (h_o, w_o) in last_avail:
                for (h_n, w_n) in avail:
                    if h_o==h_n or w_o==w_n:
                        dp[h_n][w_n] += dp[h_o][w_o]
            last_avail = avail
        return dp[height-1][width-1]           

