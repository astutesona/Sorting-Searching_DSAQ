from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        dq = deque()      # chain heads (indices), front = leftmost
        r = n - 1
        cost = 0
        ans = 0

        for l in range(n - 1, -1, -1):
            # nums[l] dominates heads with value <= nums[l]
            while dq and nums[dq[0]] <= nums[l]:
                p = dq.popleft()
                end = dq[0] - 1 if dq else r
                cost -= nums[p] * (end - p + 1) - (pre[end + 1] - pre[p])

            # add the new segment starting at l
            end = dq[0] - 1 if dq else r
            cost += nums[l] * (end - l + 1) - (pre[end + 1] - pre[l])
            dq.appendleft(l)

            # shrink right end until affordable
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans
