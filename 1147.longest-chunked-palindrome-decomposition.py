#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        input_len = len(text)
        if input_len == 0:
            return 0
        elif input_len == 1:
            return 1

        else:
            result_cnt = 0
            left_pnt = 0
            right_pnt = input_len - 1

            left_word = ''
            right_word = ''
            while left_pnt < right_pnt:
                left_word += text[left_pnt]
                right_word = text[right_pnt] + right_word

                left_pnt += 1
                right_pnt -= 1

                if left_word == right_word:
                    result_cnt += 2
                    left_word = ''
                    right_word = ''
                else:
                    if left_pnt > right_pnt:
                        result_cnt += 1
                
            
            if left_pnt == right_pnt:
                result_cnt += 1
            return result_cnt

