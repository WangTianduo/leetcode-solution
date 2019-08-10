#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])
        if width == 0:
            return False

        left = 0
        right = height - 1

        while left < right:

            mid = (left + right) // 2

            if matrix[mid][0] - target == 0:
                return True
            elif matrix[mid][0] - target < 0:
                if matrix[mid][width-1] - target == 0:
                    return True
                elif matrix[mid][width-1] - target < 0:
                    left = max(mid, left + 1)
                else:
                    break

            else:
                right = mid
        
        if left == right:
            mid = left
        
        line_idx = mid
        left = 0
        right = width - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[line_idx][mid]-target == 0:
                return True
            elif matrix[line_idx][mid] - target < 0:
                left = max(mid, left+1)
            else:
                right = mid
        
        if matrix[line_idx][left] == target:
            return True
        else:
            return False

                

