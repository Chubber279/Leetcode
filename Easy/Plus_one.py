from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        new_list = []
        for i in range(len(digits)):
            num += digits.pop() * pow(10, i)
        num += 1
        while num > 0:
            new_list.insert(0, num % 10)
            num = num // 10
        return new_list

solution = Solution()
answer = solution.plusOne([1,2,3])
print(answer)