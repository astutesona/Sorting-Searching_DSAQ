class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        # Try every possible translation
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):

                overlap = 0

                # Check every cell of img1
                for r in range(n):
                    for c in range(n):

                        if img1[r][c] == 1:
                            nr = r + dr
                            nc = c + dc

                            # Check if translated position is inside img2
                            if 0 <= nr < n and 0 <= nc < n:
                                if img2[nr][nc] == 1:
                                    overlap += 1

                ans = max(ans, overlap)

        return ans
