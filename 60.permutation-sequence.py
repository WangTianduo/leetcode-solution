#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def get_permute(n):
            result = 1
            while n > 1:
                result *= n
                n -= 1
            return result

        def get_idx(n, k):
            if n > 0:
                # print(k)
                output = list()
                cnt = 0
                while k > 0:
                    if k - get_permute(n) < 0:
                        break
                    
                    k -= get_permute(n)
                    cnt += 1
                output.append(cnt)
                return output+get_idx(n-1, k)
            else:
                return [0]
        
        idx_ls = get_idx(n-1, k-1)
        # idx_ls.append(0)
        used = list()

        result = ''
        num_ls = [x for x in range(1, n+1)]
        for idx in idx_ls:
            
            result += str(num_ls[idx])
            del(num_ls[idx])

        return result
        


