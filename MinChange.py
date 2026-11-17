class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # divisors[length] = valid d values (1 <= d < length, d divides length)
        divs = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divs[length].append(d)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in divs[length]:
                    m = length // d
                    changes = 0
                    for g in range(d):
                        l = i + g
                        r = i + g + (m - 1) * d
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    best = min(best, changes)
                cost[i][j] = best

        # dp[i][j] = min cost to split first i chars into j parts
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i // 2, k) + 1):
                for p in range(2 * (j - 1), i - 1):
                    if dp[p][j - 1] < INF and cost[p][i - 1] < INF:
                        dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]
