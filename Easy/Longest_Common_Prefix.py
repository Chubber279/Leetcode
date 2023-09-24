from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs.pop(0)
        for word in strs:
            for index in range(len(lcp)):
                if lcp == word[:len(lcp)]:
                    break
                else:
                    lcp = lcp[:len(lcp) - 1]
        return lcp

    def bestSolution(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 0:
            return ""
        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            char = strs[0][i]
            if all(c[i] == char for c in strs):
                lcp += char
            else:
                break
        return lcp
        
solution = Solution()
print(solution.longestCommonPrefix(["cir","car"]))
