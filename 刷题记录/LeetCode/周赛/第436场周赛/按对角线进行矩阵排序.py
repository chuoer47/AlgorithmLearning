from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # 先处理右上角的对角线
        for i in range(1, n):
            tmp = []
            x, y = 0, i
            while x < n and y < n:
                tmp.append(grid[x][y])
                x, y = x + 1, y + 1
            tmp.sort()
            j, x, y = 0, 0, i
            while x < n and y < n:
                grid[x][y] = tmp[j]
                j, x, y = j + 1, x + 1, y + 1
        # 处理左下角三角形
        for i in range(n):
            tmp = []
            x, y = i, 0
            while x < n and y < n:
                tmp.append(grid[x][y])
                x, y = x + 1, y + 1
            tmp.sort(reverse=True)
            j, x, y = 0, i, 0
            while x < n and y < n:
                grid[x][y] = tmp[j]
                j, x, y = j + 1, x + 1, y + 1
        return grid
