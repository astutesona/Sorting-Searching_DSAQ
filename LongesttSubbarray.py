class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # If frequency exceeds k, shrink the window
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is valid
            max_len = max(max_len, right - left + 1)

        return max_len
