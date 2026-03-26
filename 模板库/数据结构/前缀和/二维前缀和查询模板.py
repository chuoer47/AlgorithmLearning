from typing import List


class NumMatrix:
    """
    二维区域和检索类，用于高效计算矩阵中任意子矩形区域的元素和

    采用前缀和（Prefix Sum）技术，将每次区域和查询的时间复杂度优化至 O(1)，
    初始化时构建前缀和矩阵，时间复杂度为 O(n*m)，其中 n 和 m 分别为矩阵的行数和列数。
    """

    def __init__(self, matrix: List[List[int]]):
        """
        初始化前缀和矩阵

        参数:
            matrix: 输入的二维整数矩阵，假设矩阵非空且每行长度一致
        """
        # 获取矩阵的行数n和列数m
        n, m = len(matrix), len(matrix[0]) if matrix else 0

        # 构建(n+1)x(m+1)的前缀和矩阵pi，额外添加一行一列便于处理边界条件
        # pi[i][j] 表示原矩阵中从(0,0)到(i-1,j-1)的矩形区域的元素和
        self.pi = [[0] * (m + 1) for _ in range(n + 1)]

        # 填充前缀和矩阵
        for i in range(n):
            for j in range(m):
                # 前缀和计算公式：
                # 当前位置前缀和 = 上方区域前缀和 + 左方区域前缀和 - 左上角重叠区域前缀和 + 当前元素值
                self.pi[i + 1][j + 1] = self.pi[i][j + 1] + self.pi[i + 1][j] - self.pi[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        计算指定子矩形区域的元素和

        参数:
            row1: 子矩形左上角的行索引
            col1: 子矩形左上角的列索引
            row2: 子矩形右下角的行索引
            col2: 子矩形右下角的列索引

        返回:
            子矩形区域内所有元素的和
        """
        # 利用前缀和矩阵计算区域和：
        # 目标区域和 = 右下角前缀和 - 上方区域前缀和 - 左方区域前缀和 + 左上角重叠区域前缀和
        return self.pi[row2 + 1][col2 + 1] - self.pi[row1][col2 + 1] - self.pi[row2 + 1][col1] + self.pi[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)