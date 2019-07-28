#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num_letter_map = dict()

        num_letter_map['2'] = ['a', 'b', 'c']
        num_letter_map['3'] = ['d', 'e', 'f']
        num_letter_map['4'] = ['g', 'h', 'i']
        num_letter_map['5'] = ['j', 'k', 'l']
        num_letter_map['6'] = ['m', 'n', 'o']
        num_letter_map['7'] = ['p', 'q', 'r', 's']
        num_letter_map['8'] = ['t', 'u', 'v']
        num_letter_map['9'] = ['w', 'x', 'y', 'z']

        def permute(ls1, ls2):
            if ls1 == []:
                return ls2
            elif ls2 == []:
                return ls1
            else:
                output = []
                for l1 in ls1:
                    for l2 in ls2:
                        output.append(l1+l2)
            return output
            
        output = []
        for digit in digits:
            output = permute(output, num_letter_map[digit])

        return output

