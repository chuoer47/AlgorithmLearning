from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        block = []
        for i in range(x, x + k):
            row = grid[i][y:y + k]
            block.append(row)
        for i in range(x, x + k):
            grid[i][y:y + k] = block.pop()
        return grid
