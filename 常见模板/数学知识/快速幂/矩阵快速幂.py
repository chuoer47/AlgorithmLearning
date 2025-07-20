class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("矩阵维度不匹配，无法相乘")
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def power(self, n):
        # 初始化单位矩阵
        identity = [[1 if i == j else 0 for j in range(self.rows)] for i in range(self.rows)]
        result = Matrix(identity)
        current = self
        while n:
            if n % 2 == 1:
                result = result * current
            current = current * current
            n //= 2
        return result
