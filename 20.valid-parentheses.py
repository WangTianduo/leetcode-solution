#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        left_match = dict()
        right_match = dict()

        left_match['('] = ')'
        right_match[')'] = '('
        left_match['['] = ']'
        right_match[']'] = '['
        left_match['{'] = '}'
        right_match['}'] = '{'

        stack = list()
        for i in range(len(s)):
            if s[i] in left_match:
                stack.append(s[i])
            if s[i] in right_match:
                if len(stack) == 0:
                    return False
                if right_match[s[i]] != stack[-1]:
                    return False
                else:
                    stack = stack[:-1]
        if len(stack) == 0:
            return True
        else:
            return False

