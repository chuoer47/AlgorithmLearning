from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row = []
        col = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(m):
                matrix[i][j] = 0
        for j in col:
            for i in range(n):
                matrix[i][j] = 0

