class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        while result * result <= x:
            result += 1
        return result - 1
    
    def bestSolution(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = ((start + end) // 2)
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                end = mid - 1
            else:
                start = mid + 1
        return start - 1


solution = Solution()
answer = solution.bestSolution(x = 4)
print(answer)