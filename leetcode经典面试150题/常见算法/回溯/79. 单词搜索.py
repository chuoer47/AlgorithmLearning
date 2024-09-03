from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        st = [[False] * m for _ in range(n)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def dfs(depth, x, y):
            if depth >= len(word) - 1:
                return True
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if xx < 0 or xx >= n or yy < 0 or yy >= m or st[xx][yy]:
                    continue
                if board[xx][yy] == word[depth + 1]:
                    st[xx][yy] = True
                    if dfs(depth + 1, xx, yy):
                        return True
                    st[xx][yy] = False
            return False

        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    st[i][j] = True
                    if dfs(0, i, j):
                        return True
                    st[i][j] = False

        return False

