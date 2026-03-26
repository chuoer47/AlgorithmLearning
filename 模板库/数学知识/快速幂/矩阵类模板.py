from typing import Union


class Matrix:
    """
    矩阵运算类，支持矩阵乘法和矩阵快速幂运算

    该类实现了基本的矩阵操作，包括两个矩阵的乘法以及通过快速幂算法高效计算矩阵的n次幂，
    适用于线性代数计算、动态规划中的状态转移等场景。
    """

    def __init__(self, matrix: list[list[Union[int, float]]]):
        """
        初始化矩阵对象

        参数:
            matrix: 二维列表，表示矩阵的元素（假设输入为非空矩阵，且每行长度一致）

        属性:
            self.matrix: 存储矩阵元素的二维列表
            self.rows: 矩阵的行数
            self.cols: 矩阵的列数
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """
        重载乘法运算符，实现两个矩阵的乘法

        矩阵乘法规则：若A为m×n矩阵，B为n×p矩阵，则乘积C为m×p矩阵，
        其中C[i][j] = Σ(A[i][k] * B[k][j]) （k从0到n-1）

        参数:
            other: 另一个Matrix对象，作为乘法的右操作数

        返回:
            Matrix: 两个矩阵相乘的结果

        异常:
            ValueError: 当左矩阵的列数与右矩阵的行数不相等时抛出（维度不匹配）
        """
        if self.cols != other.rows:
            raise ValueError(f"矩阵维度不匹配，无法相乘。左矩阵列数={self.cols}，右矩阵行数={other.rows}")

        # 初始化结果矩阵（self.rows行，other.cols列）
        result = [[0] * other.cols for _ in range(self.rows)]

        # 计算矩阵乘积
        for i in range(self.rows):
            for j in range(other.cols):
                # 累加计算result[i][j]
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)

    def power(self, n: int) -> 'Matrix':
        """
        使用快速幂算法计算矩阵的n次幂（self^n）

        快速幂算法通过将指数n分解为二进制，减少乘法运算次数，时间复杂度为O(log n)，
        其中每次乘法的复杂度为O(m^3)（m为矩阵的阶数，假设为方阵）。

        参数:
            n: 非负整数，幂次（n=0时返回单位矩阵，n≥1时返回矩阵的n次乘积）

        返回:
            Matrix: 矩阵的n次幂结果

        注意:
            仅支持方阵（行数=列数）的幂运算，否则在乘法步骤会抛出维度不匹配异常
        """
        if n < 0:
            raise ValueError("幂次n必须为非负整数")

        # 初始化结果为单位矩阵（与self同阶的单位矩阵）
        identity = [[1 if i == j else 0 for j in range(self.rows)] for i in range(self.rows)]
        result = Matrix(identity)

        # 当前待乘的矩阵（初始为self）
        current = self

        # 快速幂核心逻辑：将n按二进制分解
        while n > 0:
            # 若当前二进制位为1，则乘以current
            if n % 2 == 1:
                result = result * current
            # current自乘（平方），对应二进制位左移
            current = current * current
            # n右移一位（整除2）
            n = n // 2

        return result


# 使用示例
if __name__ == "__main__":
    # 示例1：矩阵乘法
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = A * B
    print("矩阵A * B的结果：")
    for row in C.matrix:
        print(row)  # 输出：[[19, 22], [43, 50]]

    # 示例2：矩阵快速幂（计算A^3）
    A3 = A.power(3)
    print("\n矩阵A^3的结果：")
    for row in A3.matrix:
        print(row)  # 输出：[[37, 54], [81, 118]]

    # 示例3：单位矩阵验证（A^0为单位矩阵）
    A0 = A.power(0)
    print("\n矩阵A^0（单位矩阵）的结果：")
    for row in A0.matrix:
        print(row)  # 输出：[[1, 0], [0, 1]]