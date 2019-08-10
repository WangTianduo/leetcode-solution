#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            slow_pnt = 0
            fast_pnt = 1

            substring = s[slow_pnt:fast_pnt]
            length = 1
            max_len = length
            while fast_pnt < len(s):
                fast_pnt += 1
                if s[fast_pnt - 1] in substring:
                    slow_gap = substring.find(s[fast_pnt-1])
                    slow_pnt += slow_gap + 1
                    substring = s[slow_pnt: fast_pnt]
                    length = len(substring)
                else:
                    substring = s[slow_pnt: fast_pnt]
                    length += 1
                    if length > max_len:
                        max_len = length

            return max_len


