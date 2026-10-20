from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            ok = True
            prev_max = 0  # nums[i] >= 1, so 0 is a safe initial value

            for s in range(0, n, k):
                e = s + k
                descents = 0
                mn = nums[s]
                mx = nums[s]

                for i in range(s, e - 1):
                    if nums[i] > nums[i + 1]:
                        descents += 1
                        if descents > 1:
                            break
                    v = nums[i + 1]
                    if v < mn:
                        mn = v
                    elif v > mx:
                        mx = v

                if descents > 1:
                    ok = False
                    break

                # wrap-around descent (never triggers for k == 1)
                if k > 1 and nums[e - 1] > nums[s]:
                    descents += 1
                    if descents > 1:
                        ok = False
                        break

                # blocks must chain in sorted order
                if mn < prev_max:
                    ok = False
                    break
                prev_max = mx

            if ok:
                total += k

        return total
