class BinaryIndexedTree:
    """
    树状数组（Binary Indexed Tree，BIT）实现

    树状数组是一种高效的数据结构，用于快速处理前缀和查询与单点更新操作，
    时间复杂度均为O(log n)，适用于需要频繁进行这两种操作的场景。
    """
    # 限制类的属性，仅允许n和c，优化内存和访问速度
    __slots__ = ["n", "c"]

    def __init__(self, n):
        """
        初始化树状数组

        参数:
            n: 树状数组的大小（处理的元素范围为1..n）
        """
        self.n = n  # 记录数组大小
        # 初始化树状数组存储结构，索引从1开始，故长度为n+1
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int):
        """
        单点更新：将位置x的元素增加delta

        参数:
            x: 要更新的位置（1-based索引）
            delta: 增加的值（可为正或负）
        """
        # 从x开始，沿树状数组的索引路径向上更新
        while x <= self.n:
            self.c[x] += delta  # 更新当前节点
            # x & -x 得到x的最低位1，用于计算下一个需要更新的节点
            x += x & -x

    def query(self, x: int) -> int:
        """
        前缀和查询：计算从1到x的元素总和

        参数:
            x: 前缀的结束位置（1-based索引）

        返回:
            1到x的元素之和
        """
        s = 0  # 存储前缀和结果
        # 从x开始，沿树状数组的索引路径向下累加
        while x > 0:
            s += self.c[x]  # 累加当前节点的值
            # x & -x 得到x的最低位1，用于计算下一个需要累加的节点
            x -= x & -x
        return s