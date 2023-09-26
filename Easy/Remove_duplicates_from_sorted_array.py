from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1




solution = Solution()
print(solution.removeDuplicates([1,1,2]))