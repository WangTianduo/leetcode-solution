#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        if height == 0:
            return
        width = len(matrix[0])

        if width == 0:
            return
        elif height == 1:
            return matrix[0]
        elif width == 1:
            result = []
            for line in matrix:
                result.append(line[0])
            return result
        else:
            result = []
            cnt = 0
            pnt = [0, 0]
            while cnt < height * width:
                while pnt[1] < width and matrix[pnt[0]][pnt[1]] != '*':
                    result.append(matrix[pnt[0]][pnt[1]])
                    matrix[pnt[0]][pnt[1]] = '*'
                    pnt[1] += 1
                    cnt += 1
                pnt[1] -= 1
                pnt[0] += 1
                while pnt[0] < height and matrix[pnt[0]][pnt[1]] != '*':
                    result.append(matrix[pnt[0]][pnt[1]])
                    matrix[pnt[0]][pnt[1]] = '*'
                    pnt[0] += 1
                    cnt += 1
                pnt[0] -= 1
                pnt[1] -= 1
                while pnt[1] >= 0 and matrix[pnt[0]][pnt[1]] != '*':
                    result.append(matrix[pnt[0]][pnt[1]])
                    matrix[pnt[0]][pnt[1]] = '*'
                    pnt[1] -= 1
                    cnt += 1
                pnt[1] += 1
                pnt[0] -= 1
                while matrix[pnt[0]][pnt[1]] != '*':
                    result.append(matrix[pnt[0]][pnt[1]])
                    matrix[pnt[0]][pnt[1]] = '*'
                    pnt[0] -= 1
                    cnt += 1
                pnt[0] += 1
                pnt[1] += 1
            return result
                
        

