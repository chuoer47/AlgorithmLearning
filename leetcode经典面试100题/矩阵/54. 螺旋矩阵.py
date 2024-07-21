"""
https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150


"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        choices = {
            "left": [0, -1],
            "right": [0, 1],
            "up": [-1, 0],
            "down": [1, 0]
        }
        trans = {
            "right": "down",
            "left": "up",
            "up": "right",
            "down": "left"
        }
        n, m = len(matrix), len(matrix[0])
        flag = [[0] * m for _ in range(n)]
        path = []
        now = "right"
        x, y = 0, -1
        while True:
            dx, dy = choices[now]
            if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1:
                if not flag[x + dx][y + dy]:
                    x, y = x + dx, y + dy
                    flag[x][y] = 1
                    path.append(matrix[x][y])
                else:
                    now = trans[now]
            else:
                now = trans[now]
            if len(path) == n * m:
                break
        return path


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    s = Solution()
    print(s.spiralOrder(matrix))
