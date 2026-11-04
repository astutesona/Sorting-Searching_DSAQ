from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        cnt = [0] * (m + 1)   # BIT of counts
        sm = [0] * (m + 1)    # BIT of sums

        def update(i, c, v):
            while i <= m:
                cnt[i] += c
                sm[i] += v
                i += i & -i

        LOG = 1
        while (LOG << 1) <= m:
            LOG <<= 1

        def kth(t):
            # value of t-th smallest (1-indexed)
            pos = 0
            pw = LOG
            while pw:
                np_ = pos + pw
                if np_ <= m and cnt[np_] < t:
                    pos = np_
                    t -= cnt[np_]
                pw >>= 1
            return pos + 1  # rank of the element

        def query(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        W = n - x + 1
        cost = [0] * W
        total = 0
        target = (x + 1) // 2

        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth(target)
                med = vals[r - 1]
                c_le, s_le = query(r)
                cost[i - x + 1] = (med * c_le - s_le) + ((total - s_le) - med * (x - c_le))

        INF = float('inf')
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    p = prev[i - x]
                    if p != INF:
                        v = p + cost[i - x]
                        if v < best:
                            best = v
                cur[i] = best
            prev = cur
        return prev[n]
