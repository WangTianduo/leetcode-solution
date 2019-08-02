#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result_ls = list()

        def helper(left_num, right_num, half_result):
            result = []
            # half_result: string
            if left_num == right_num == 0:
                return [half_result]
            elif left_num < 0 or right_num < 0:
                return []
            elif left_num == 0:
                half_result += ')' * right_num
                return [half_result]
            elif left_num == right_num:
                
                half_result += '('
                
                temp1 = half_result + '('
                result1 = helper(left_num-2, right_num, temp1)
                temp2 = half_result + ')'
                result2 = helper(left_num-1, right_num-1, temp2)
                if len(result1) > 0:
                    result.extend(result1)
                if len(result2) > 0:
                    result.extend(result2)
            else:
                temp1 = half_result + '('
                result1 = helper(left_num-1, right_num, temp1)
                temp2 = half_result + ')'
                result2 = helper(left_num, right_num-1, temp2)
                if len(result1) > 0:
                    result.extend(result1)
                if len(result2) > 0:
                    result.extend(result2)
            
            return result

        ls = helper(n, n, '')
        return ls         

