from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = []
        for i in range(m):
            if i == 0:
                # First row: all free
                grid.append('.' * n)
            else:
                # Other rows: obstacles except the last column
                grid.append('#' * (n - 1) + '.')
        return grid
