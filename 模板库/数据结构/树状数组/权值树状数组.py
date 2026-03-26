import math
from math import inf


class BinaryIndexedMaxTree:
    """
    用于维护前缀最大值的树状数组（Binary Indexed Tree，BIT）实现

    这是树状数组的变种，专门用于高效处理单点更新（更新为更大值）和前缀最大值查询操作，
    时间复杂度均为O(log n)，适用于需要频繁查询某段前缀的最大值或更新单点值的场景。
    """
    # 限制类的属性，仅允许n和c，优化内存和访问速度
    __slots__ = ["n", "c"]

    def __init__(self, n):
        """
        初始化最大值树状数组

        参数:
            n: 树状数组的大小（处理的元素范围为1..n）
        """
        self.n = n  # 记录数组大小（1-based索引范围）
        # 初始化树状数组存储结构，索引从1开始，初始值为负无穷（因需维护最大值，初始为最小可能值）
        self.c = [-inf] * (n + 1)

    def update(self, x: int, delta: int):
        """
        单点更新：将位置x的元素更新为当前值与delta中的最大值

        参数:
            x: 要更新的位置（1-based索引）
            delta: 用于更新的候选值（若delta大于当前位置的最大值，则更新）
        """
        # 从x开始，沿树状数组的索引路径向上更新
        while x <= self.n:
            # 当前节点存储的是对应区间的最大值，取当前值与delta的较大者
            self.c[x] = max(self.c[x], delta)
            # x & -x 得到x的最低位1，用于计算下一个需要更新的节点（树状数组的索引跳转）
            x += x & -x

    def query(self, x: int):
        """
        前缀最大值查询：计算从1到x的元素中的最大值

        参数:
            x: 前缀的结束位置（1-based索引）

        返回:
            1到x范围内的最大值（若范围内无有效元素，返回- inf）
        """
        s = -inf  # 存储前缀最大值结果，初始为负无穷
        # 从x开始，沿树状数组的索引路径向下收集最大值
        while x > 0:
            # 取当前节点的最大值与已有结果的较大者
            s = max(s, self.c[x])
            # x & -x 得到x的最低位1，用于计算下一个需要查询的节点
            x -= x & -x
        return s
