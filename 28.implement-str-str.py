#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            for idx in range(len(haystack)):
                if haystack[idx] == needle[0] and haystack[idx:idx+len(needle)] == needle:
                    return idx
            return -1

