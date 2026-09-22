class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node:
        # [product modulo k, count of prefix products for each remainder]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            # Product of the whole combined segment
            prod = (lp * rp) % k

            cnt = lc[:]

            # Prefixes that contain all of left
            # and then some prefix of right
            for r in range(k):
                new_r = (lp * r) % k
                cnt[new_r] += rc[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                tree[node][0] = rem
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                rem = value % k

                tree[node][0] = rem
                tree[node][1] = [0] * k
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            # Completely outside
            if r < ql or l > qr:
                return None

            # Completely inside
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            if left is None:
                return right

            if right is None:
                return left

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            update(1, 0, n - 1, index, value)

            # We need all non-empty prefixes of nums[start:]
            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans
