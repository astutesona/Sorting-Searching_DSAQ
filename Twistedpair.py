from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]
        R[0][0] = 1  # start counts as one way (grid[0][0] is empty)

        for i in range(m):
            for j in range(n):
                r, d = R[i][j], D[i][j]
                if grid[i][j] == 0:
                    t = (r + d) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + t) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + t) % MOD
                else:
                    # entered moving right -> pushed down
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + r) % MOD
                    # entered moving down -> pushed right
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + d) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD
