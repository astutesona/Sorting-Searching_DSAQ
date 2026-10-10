
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        operations = sum(max(0, d - level) for d in diff)

        # Reduce the remaining differences above the final level.
        # The binary search level is feasible, but level - 1 is not.
        remaining = k - operations

        ans = 0
        for d in diff:
            reduced = min(d, level)
            ans += reduced * reduced

        # Use the remaining operations to reduce level to level - 1.
        ans -= remaining * (2 * level - 1)

        return ans
