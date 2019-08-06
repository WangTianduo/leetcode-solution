#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
        
        ls1 = [int(x) for x in num1]
        ls2 = [int(x) for x in num2]

        ls1.reverse()
        ls2.reverse()

        result = 0
        for idx1 in range(len(ls1)):
            for idx2 in range(len(ls2)):
                result += ls1[idx1]*ls2[idx2]*10**(idx1+idx2)
        return str(result)

