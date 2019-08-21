#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        temp = 0
        ptr = 0

        a = a[::-1]
        b = b[::-1]

        result = ''
        while True:
           
            if ptr == len(a) or ptr == len(b):
                break
            else:
                num1 = a[ptr]
                num2 = b[ptr]

                digit = int(num1)+int(num2)+temp
                if digit == 0:
                    result += '0'
                elif digit == 1:
                    result += '1'
                    temp = 0
                elif digit == 2:
                    result += '0'
                    temp = 1
                else:
                    result += '1'
                    temp = 1
                ptr += 1
        
        if len(a) > len(b):
            while temp == 1 and ptr < len(a):
                digit = temp + int(a[ptr])
                if digit == 1:
                    temp = 0
                    result += '1'
                else:
                    result += '0'
                ptr += 1
            result += a[ptr:]

        elif len(a) == len(b):
            if temp == 1:
                result += '1'
                temp = 0
        else:
            while temp == 1 and ptr < len(b):
                digit = temp + int(b[ptr])
                if digit == 1:
                    temp = 0
                    result += '1'
                else:
                    result += '0'
                ptr += 1
            result += b[ptr:]
        if temp == 1:
            result += '1'
        return result[::-1]


