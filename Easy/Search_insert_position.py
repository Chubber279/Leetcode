from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        index = 0
        while index < len(nums) and nums[index] < target:
            index += 1
        return index
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpoint = start + (end - start) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
            else:
                end = midpoint - 1
        return start
solution = Solution()
answer = solution.searchInsert(nums = [1,3,5,6], target = 5)
print(answer)