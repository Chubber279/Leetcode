class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if haystack == needle:
            return 0
        if len(haystack) <= len(needle):
            return index
        for i in range(len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                return i
        return -1
    
    def find_method(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        return index
    
    def index_method(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
            return index
        except ValueError:
            return -1
        
solution = Solution()
answer = solution.strStr(haystack = "abc", needle = "c")
print(answer)