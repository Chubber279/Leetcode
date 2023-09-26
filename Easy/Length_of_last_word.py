class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.rstrip().split(" ")
        return len(words_list[len(words_list) - 1])

solution = Solution()
answer = solution.lengthOfLastWord(s = "Hello World")
print(answer)