from functools import reduce
from typing import Callable, List, Any


class SparseTable:
    """
    稀疏表（Sparse Table）数据结构实现，支持静态区间查询操作

    稀疏表基于倍增思想，通过预处理构建多层区间信息，实现O(1)时间复杂度的区间查询，
    适用于满足**结合律**和**幂等性**的操作（如区间最大值、最小值、gcd、按位与、按位或等）。
    预处理时间复杂度为O(n log n)，空间复杂度为O(n log n)，支持静态数据（构建后不可修改）。
    """

    def __init__(self, data: list, func: Callable[[Any, Any], Any] = lambda x, y: x | y):
        """
        初始化稀疏表

        参数:
            data: 输入的静态数据列表（下标从0开始），需为可迭代对象
            func: 区间查询的合并函数，需满足结合律和幂等性（如max、min、gcd、lambda x,y:x|y等）
                  默认为按位或操作（lambda x,y: x|y）

        预处理过程:
            1. 构建多层区间信息表`st`，其中`st[k][i]`表示以`i`为起点、长度为`2^k`的区间的合并结果
            2. 第0层（k=0）直接存储原始数据（长度为`2^0=1`的区间）
            3. 第k层（k>0）通过合并第k-1层中两个相邻的、长度为`2^(k-1)`的区间构建，即：
               `st[k][i] = func(st[k-1][i], st[k-1][i + 2^(k-1)])`
            4. 层数由数据长度决定，最大层数为`log2(n)`（n为data长度）
        """
        self.func = func  # 区间合并函数
        self.st = [list(data)]  # 稀疏表核心存储，st[k]为第k层区间信息
        i, n = 1, len(self.st[0])  # i为当前层数对应的步长（2^i），n为数据长度

        # 构建多层区间信息，直到步长的2倍超过数据长度
        while 2 * i <= n:
            prev_layer = self.st[-1]  # 上一层的区间信息
            # 第k层的每个区间由上一层两个长度为i的区间合并而成
            curr_layer = [
                self.func(prev_layer[j], prev_layer[j + i])
                for j in range(n - 2 * i + 1)
            ]
            self.st.append(curr_layer)
            i <<= 1  # 步长倍增（i = 2^k）

    def query(self, begin: int, end: int) -> Any:
        """
        查询闭区间[begin, end]的合并结果（结果由初始化时的func决定）

        参数:
            begin: 区间左端点（0-based索引，包含在区间内）
            end: 区间右端点（0-based索引，包含在区间内）

        返回:
            区间[begin, end]经func合并后的结果

        实现逻辑:
            1. 计算区间长度：length = end - begin + 1
            2. 求最大k值：满足2^k ≤ length（通过bit_length快速计算lg(length)）
            3. 取两个长度为2^k的区间覆盖[begin, end]：
               - 第一个区间：[begin, begin + 2^k - 1]
               - 第二个区间：[end - 2^k + 1, end]
            4. 用func合并两个区间的结果，即为查询结果
        """
        if begin < 0 or end >= len(self.st[0]) or begin > end:
            raise ValueError(f"无效区间 [{begin}, {end}]，有效范围为[0, {len(self.st[0]) - 1}]")

        length = end - begin + 1
        lg = length.bit_length() - 1  # 等价于floor(log2(length))
        # 合并两个覆盖区间的结果
        return self.func(
            self.st[lg][begin],
            self.st[lg][end - (1 << lg) + 1]  # 1 << lg 等价于2^lg
        )


# 使用示例
if __name__ == "__main__":
    # 示例1：区间最大值查询
    data_max = [3, 1, 4, 1, 5, 9, 2, 6]
    st_max = SparseTable(data_max, func=max)
    print("区间最大值查询：")
    print(f"[0, 7] = {st_max.query(0, 7)}")  # max(3,1,4,1,5,9,2,6) = 9
    print(f"[2, 5] = {st_max.query(2, 5)}")  # max(4,1,5,9) = 9

    # 示例2：区间gcd查询（需传入gcd函数）
    from math import gcd

    data_gcd = [12, 18, 6, 24, 36]
    # 注意：gcd函数需包装为接收两个参数的函数
    st_gcd = SparseTable(data_gcd, func=lambda a, b: gcd(a, b))
    print("\n区间gcd查询：")
    print(f"[0, 4] = {st_gcd.query(0, 4)}")  # gcd(12,18,6,24,36) = 6
    print(f"[1, 3] = {st_gcd.query(1, 3)}")  # gcd(18,6,24) = 6

    # 示例3：区间按位或查询（默认func为按位或）
    data_or = [1, 2, 4, 8]
    st_or = SparseTable(data_or)  # 默认func=lambda x,y: x|y
    print("\n区间按位或查询：")
    print(f"[0, 3] = {st_or.query(0, 3)}")  # 1 | 2 | 4 | 8 = 15
    print(f"[1, 2] = {st_or.query(1, 2)}")  # 2 | 4 = 6