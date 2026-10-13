from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(x * x for x in nums)

        n = len(nums)
        half = n // 2

        return sum(nums[half:]) - sum(nums[:half])
