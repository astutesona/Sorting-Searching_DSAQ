class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        # prefix[i] = sum of nums[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')
        for i in range(n):
            # subarray nums[i..j], length = j - i + 1
            for length in range(l, r + 1):
                j = i + length
                if j > n:
                    break
                s = prefix[j] - prefix[i]
                if s > 0:
                    ans = min(ans, s)

        return -1 if ans == float('inf') else ans
