import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0

        # adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K1 = k + 1                      # run lengths are 1..k
        INF = float('inf')
        dist = [INF] * (n * K1)

        dist[1] = 0                     # state (node 0, run 1)
        heap = [(0, 0, 1)]              # (cost, node, run)
        target = n - 1

        while heap:
            d, u, r = heapq.heappop(heap)
            if d > dist[u * K1 + r]:
                continue
            if u == target:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                if labels[v] == lu:
                    nr = r + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                idx = v * K1 + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, v, nr))

        return -1
