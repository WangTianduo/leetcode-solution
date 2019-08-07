#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        distance = dict()
        def get_distance(h, w, grid, distance):
            if (h, w) in distance:
                return distance[(h, w)]
            elif h == 0 and w == 0:
                distance[(h, w)] = grid[0][0]
                return distance[(h, w)]
            elif h == 0:
                distance[(h, w)] = sum(grid[h][0:w+1])
                return distance[(h, w)]

            elif w == 0:
                distance[(h, w)] = sum([grid[hi][w] for hi in range(h+1)])
                return distance[(h, w)]
            else:
                distance[(h, w)] = grid[h][w] + min(get_distance(h-1, w, grid, distance), 
                                        get_distance(h, w-1, grid, distance))
                return distance[(h, w)]

        return get_distance(height-1, width-1, grid, distance)

