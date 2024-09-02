from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        next = [[0] * m for _ in range(n)]

        def count(i, j):
            ans = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue
                    if board[x][y] == 1:
                        ans += 1
            return ans

        for i in range(n):
            for j in range(m):
                cnt = count(i, j)
                if board[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        next[i][j] = 0
                    else:
                        next[i][j] = 1
                else:
                    if cnt == 3:
                        next[i][j] = 1
                    else:
                        next[i][j] = 0
        board[:] = next
