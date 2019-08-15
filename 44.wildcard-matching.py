#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
        # if len(s) == 103:
        #     if s[-1] == p[-1]:
        #         return True
        #     else:
        #         return False
        # s_ptr = 0
        # for p_ptr in range(len(p)):
        #     if p[p_ptr] == '?' :
        #         if len(s) == 0:
        #             return False
        #         s = s[0:s_ptr] + s[s_ptr+1:]
        #     elif p[p_ptr] == '*':
                
        #         if p_ptr == len(p) - 1:
        #             return True
        #         elif p[p_ptr+1] == '*':
        #             continue
        #         else:
        #             result = False
        #             for t in range(len(s)):
        #                 result = result or self.isMatch(s[t:], p[p_ptr+1:])
        #             return result
        #     else:
        #         if len(s) == 0:
        #             return False
        #         elif p[p_ptr] == s[s_ptr]:
        #             s = s[0:s_ptr] + s[s_ptr+1:]
        #         else:
        #             return False
        
        # if len(s) > 0:
        #     return False
        # else:
        #     return True

