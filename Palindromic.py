from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        LOG = max(1, n.bit_length())
        par = [0] * n
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        base = [0] * n
        idx = [0] * n

        chars = [1 << (ord(c) - 97) for c in s]

        # iterative DFS from root 0
        timer = 1
        base[0] = chars[0]
        stack = [0]
        while stack:
            v = stack[-1]
            if idx[v] < len(g[v]):
                to = g[v][idx[v]]
                idx[v] += 1
                if to == par[v]:
                    continue
                par[to] = v
                depth[to] = depth[v] + 1
                base[to] = base[v] ^ chars[to]
                tin[to] = timer
                timer += 1
                stack.append(to)
            else:
                tout[v] = timer - 1
                stack.pop()

        up = [par]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return par[a]

        # Fenwick tree (XOR), range-update / point-query
        size = n + 2
        bit = [0] * (size + 1)

        def upd(i: int, val: int) -> None:
            i += 1
            while i <= size:
                bit[i] ^= val
                i += i & -i

        def qry(i: int) -> int:
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                d = chars[u] ^ new
                if d:
                    chars[u] = new
                    upd(tin[u], d)
                    upd(tout[u] + 1, d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = base[u] ^ qry(tin[u]) ^ base[v] ^ qry(tin[v]) ^ chars[l]
                ans.append(m & (m - 1) == 0)
        return ans
