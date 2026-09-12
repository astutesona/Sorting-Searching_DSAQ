from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: [start, end, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by starting point
        arr.sort()

        starts = [x[0] for x in arr]

        # dp[k][i] = best answer using intervals from i onward
        # with at most k intervals.
        #
        # Store (score, indices)
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):

                # Option 1: skip current interval
                best_score, best_indices = dp[k][i + 1]

                l, r, w, idx = arr[i]

                # Find first interval whose start > r
                # because sharing boundary means overlapping.
                nxt = bisect_right(starts, r)

                # Option 2: take current interval
                take_score = w + dp[k - 1][nxt][0]
                take_indices = [idx] + dp[k - 1][nxt][1]

                # Compare by score first, then lexicographically
                if take_score > best_score:
                    dp[k][i] = (take_score, take_indices)
                elif take_score < best_score:
                    dp[k][i] = (best_score, best_indices)
                else:
                    if sorted(take_indices) < sorted(best_indices):
                        dp[k][i] = (take_score, take_indices)
                    else:
                        dp[k][i] = (best_score, best_indices)

        return sorted(dp[4][0][1])
