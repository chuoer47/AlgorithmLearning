import math
from typing import List


class STTable:
    """
    ST表（Sparse Table）实现，用于静态区间最大值查询

    核心特性：
    - 预处理时间复杂度：O(n log n)
    - 单次查询时间复杂度：O(1)
    - 仅支持静态数据（构建后不支持修改操作）
    """

    def __init__(self, data: List[int]):
        """
        初始化ST表

        参数:
            data: 静态数据列表（0-based索引）
        """
        self.n = len(data)
        if self.n == 0:
            raise ValueError("数据列表不能为空")

        # 计算log2(n)的最大值，用于确定ST表的层数
        self.k = self._get_max_k()

        # 初始化ST表：st[k][i]表示从i开始，长度为2^k的区间的最大值
        self.st = [[0] * self.n for _ in range(self.k + 1)]

        # 第0层（k=0）：区间长度为2^0=1，即单个元素自身
        for i in range(self.n):
            self.st[0][i] = data[i]

        # 填充ST表：对于每一层k，基于k-1层计算
        for j in range(1, self.k + 1):
            # 对于每个位置i，计算从i开始长度为2^j的区间最大值
            # 注意：i + 2^(j-1) 不能超出数组范围
            for i in range(self.n - (1 << j) + 1):
                # 区间[i, i+2^j-1]可分为[i, i+2^(j-1)-1]和[i+2^(j-1), i+2^j-1]
                self.st[j][i] = max(
                    self.st[j - 1][i],
                    self.st[j - 1][i + (1 << (j - 1))]
                )

        # 预计算log2值，加速查询时的k值计算
        self.log_table = self._precompute_log()

    def _get_max_k(self) -> int:
        """计算最大的k值，使得2^k <= n"""
        return max(0, math.floor(math.log2(self.n)))

    def _precompute_log(self) -> List[int]:
        """预计算log2值，log_table[i]表示floor(log2(i))"""
        log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            log_table[i] = log_table[i // 2] + 1
        return log_table

    def query(self, l: int, r: int) -> int:
        """
        查询区间[l, r]（闭区间）的最大值

        参数:
            l: 区间左端点（0-based索引）
            r: 区间右端点（0-based索引）

        返回:
            区间[l, r]的最大值

        异常:
            ValueError: 当l或r超出有效范围，或l > r时抛出
        """
        # 边界检查
        if l < 0 or r >= self.n or l > r:
            raise ValueError(f"无效的区间 [{l}, {r}]，数据范围为[0, {self.n - 1}]")

        # 计算区间长度
        length = r - l + 1

        # 计算k = floor(log2(length))，即最大的k使得2^k <= length
        k = self.log_table[length]

        # 区间[l, r]可由两个长度为2^k的区间覆盖：
        # [l, l+2^k-1] 和 [r-2^k+1, r]
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


# 使用示例
if __name__ == "__main__":
    # 测试数据
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"原始数据: {data}")

    # 创建ST表
    st = STTable(data)

    # 测试区间查询
    test_cases = [
        (0, 0),  # 单个元素：3
        (2, 5),  # [4,1,5,9] → 9
        (0, 9),  # 整个数组 → 9
        (6, 8),  # [2,6,5] → 6
        (3, 7)  # [1,5,9,2] → 9
    ]

    for l, r in test_cases:
        print(f"查询区间 [{l}, {r}] 的最大值: {st.query(l, r)}")
