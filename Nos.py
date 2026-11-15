class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0   # counts of prefix sums by parity (empty prefix is even)
        prefix = 0
        ans = 0

        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                ans += odd      # pair with earlier odd prefixes
                even += 1
            else:
                ans += even     # pair with earlier even prefixes
                odd += 1

        return ans % MOD
