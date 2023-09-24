class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True
    
    def bestSolution(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)

        return str_x == str_x[::-1]

solution = Solution()
print(solution.isPalindrome(x=121))