class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    def helper(self, n:int, memo: dict[int, int]):
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
        '''
        n = 1
        1

        n = 2
        1 + 1
        2

        n = 3
        1 + 1 + 1
        1 + 2
        2 + 1

        n = 4
        1 + 1 + 1 + 1
        1 + 2 + 1
        2 + 1 + 1
        1 + 1 + 2
        2 + 2


        
        '''

solution = Solution()
answer = solution.climbStairs(n = 44)
print(answer)