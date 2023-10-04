from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
                return []
        if numRows == 1:
            return [[1]]
        prev_row = self.generate(numRows - 1)
        new_list = [1 for _ in range(numRows)]
        for i in range(1, numRows - 1):
            new_list[i] = prev_row[numRows - 2][i - 1] + prev_row[numRows - 2][i]
        prev_row.append(new_list)
        return prev_row
        
            

solution = Solution()
answer = solution.generate(numRows=5)
print(answer)