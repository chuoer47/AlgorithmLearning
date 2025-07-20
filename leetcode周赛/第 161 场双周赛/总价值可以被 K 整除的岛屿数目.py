from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and vis[i][j] == 0:
                    sn = 0
                    q = [(i, j)]
                    while q:
                        x, y = q.pop()
                        if vis[x][y]:
                            continue
                        sn += grid[x][y]
                        vis[x][y] = 1
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == 0 and grid[xx][yy] != 0:
                                q.append((xx, yy))
                    ans += int(sn % k == 0)
        return ans
