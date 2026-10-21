class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Unsorted and length 2: the only substring we can sort is a single
        # character, which does nothing, so it's impossible.
        if n == 2:
            return -1

        mn, mx = min(s), max(s)

        # If the first char is already the minimum, sort s[1:].
        # If the last char is already the maximum, sort s[:-1].
        if s[0] == mn or s[-1] == mx:
            return 1

        # Two operations work if:
        #  - the min appears somewhere in s[0..n-2]: sort s[0..n-2], then s[1..n-1]
        #  - the max appears somewhere in s[1..n-1]: sort s[1..n-1], then s[0..n-2]
        if mn in s[:-1] or mx in s[1:]:
            return 2

        # Remaining case: the min exists only at the last index and the max
        # only at the first index (e.g. "cba"). This needs 3 operations.
        return 3
