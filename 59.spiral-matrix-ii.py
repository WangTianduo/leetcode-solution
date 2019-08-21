#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        result = [[0 for _ in range(n)]for _ in range(n)]

        cnt = 1
        pos = [0, 0]
        while cnt <= n**2:
            while pos[1] < n and result[pos[0]][pos[1]] == 0:
                result[pos[0]][pos[1]] = cnt
                cnt += 1
                pos[1] += 1
            
            pos[1] -= 1
            pos[0] += 1

            while pos[0] < n and result[pos[0]][pos[1]] == 0:
                result[pos[0]][pos[1]] = cnt
                cnt += 1
                pos[0] += 1

            pos[0] -= 1
            pos[1] -= 1

            while pos[1] >= 0 and result[pos[0]][pos[1]] == 0:
                result[pos[0]][pos[1]] = cnt
                cnt += 1
                pos[1] -= 1

            pos[1] += 1
            pos[0] -= 1

            while pos[0] >= 0 and result[pos[0]][pos[1]] == 0:
                result[pos[0]][pos[1]] = cnt
                cnt += 1
                pos[0] -= 1

            pos[0] += 1
            pos[1] += 1

        return result


