from collections import defaultdict
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)  # dp[v] = longest consecutive run ending at value v

        for x in nums:
            dp[x + 1] = dp[x] + 1      # use x as x+1 (must run first)
            dp[x] = dp[x - 1] + 1      # keep x as x

        return max(dp.values())
