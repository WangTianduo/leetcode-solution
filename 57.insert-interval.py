#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        s, e = newInterval[0], newInterval[1]

        left = [item for item in intervals if item[1]<s]
        right = [item for item in intervals if item[0] > e]

        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s,e]] + right

