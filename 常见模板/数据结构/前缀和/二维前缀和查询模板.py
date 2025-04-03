from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        pi = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pi[i][j] += pi[i - 1][j] + pi[i][j - 1] - pi[i - 1][j - 1] + matrix[i][j]
        self.pi = pi

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pi = self.pi
        return pi[row2][col2] - pi[row1 - 1][col2] - pi[row2][col1 - 1] + pi[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
