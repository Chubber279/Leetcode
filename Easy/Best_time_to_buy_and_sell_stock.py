from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0
        if len(prices) == 1:
            return 0
        minPrice = 99999999999999
        minPriceIndex = 0
        for index, price in enumerate(prices):
            if prices[right] < prices[left]:
                left = right
            if (prices[right] - prices[left]) > profit:
                profit = (prices[right] - prices[left])
            right += 1
        return profit

solution = Solution()
answer = solution.maxProfit(prices=[7,1,5,3,6,4])
print(answer)