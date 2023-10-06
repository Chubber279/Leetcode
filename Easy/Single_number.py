from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            for j in range(i+1, (len(nums))):
                if nums[i] == nums[j]:
                    nums[i] = None
                    nums[j] = None
                    break
        for i in nums:
            if i is not None:
                return i
            
    def bestSolution(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output ^= i
        return output

        
            
        

            
solution = Solution()
print(solution.singleNumber(nums = [2,2,1]))
print(solution.singleNumber(nums = [4,1,2,1,2]))
print(solution.bestSolution(nums = [1, 0, 1]))