#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split()) == 0:
            return 0
        return len(s.split()[-1])

