#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_nine_units(board):
            result = []
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    temp = [str(x) for x in range(1, 10)]

                    for sub_row in range(0, 3):
                        for sub_col in range(0, 3):
                            if board[row+sub_row][col+sub_col] != '.' and board[row+sub_row][col+sub_col] in temp:
                                temp.remove(board[row+sub_row][col+sub_col])
                    result.append(temp)
            return result

        def get_nine_rows(board):
            result = []
            for line in board:
                temp = [str(x) for x in range(1, 10)]

                for num in line:
                    if num != '.':
                        temp.remove(num)
                result.append(temp)
            return result
        
        def get_nine_cols(board):
            result = []
            for col in range(0, 9):
                temp = [str(x) for x in range(1, 10)]
                for row in range(0, 9):
                    if board[row][col] != '.':
                        temp.remove(board[row][col])
                result.append(temp)
                
            return result


        unit_set = get_nine_units(board)
        row_set = get_nine_rows(board)
        col_set = get_nine_cols(board)
    
        cnt = 0
        possible = [[[] for _ in range(9)] for _ in range(9)]
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == '.':
                    for item in row_set[row]:
                        if item in col_set[col] and item in unit_set[row//3*3+col//3]:
                            possible[row][col].append(item)

                else:
                    cnt += 1
        
        def elimate(row, col, val):
            for row_idx in range(9):
                if val in possible[row_idx][col]:
                    possible[row_idx][col].remove(val)
            for col_idx in range(9):
                if val in possible[row][col_idx]:
                    possible[row][col_idx].remove(val)
            
            start_row = row//3*3
            start_col = col//3*3

            for i in range(3):
                for j in range(3):
                    if val in possible[start_row+i][start_col+j]:
                        possible[start_row+i][start_col+j].remove(val)
        
        while cnt < 81:
            for row in range(9):
                for col in range(9):
                    if len(possible[row][col]) == 1:
                        board[row][col] = possible[row][col][0]
                        elimate(row, col, board[row][col])
                        cnt += 1

                    

