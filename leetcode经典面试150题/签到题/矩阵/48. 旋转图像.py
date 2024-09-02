from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[-j - 1][-i - 1] = matrix[-j - 1][-i - 1], matrix[i][j]
        for i in range(n // 2):
            tem = matrix[i].copy()
            matrix[i] = matrix[n-1-i].copy()
            matrix[n-1-i] = tem.copy()
        return


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    print(matrix)
