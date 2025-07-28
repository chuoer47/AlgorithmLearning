class Fenwick:
    """
    维护前缀范围内最大长度及其对应计数的树状数组（Fenwick Tree变种）

    用于高效记录和查询某个前缀范围内的最大长度值，以及该最大长度出现的总次数。
    适用于需要动态更新元素信息，并频繁查询前缀最大长度及计数的场景（如最长递增子序列计数等问题）。
    """
    __slots__ = 'mx_length', 'mx_cnt'  # 限制属性，优化内存和访问速度

    def __init__(self, n: int):
        """
        初始化树状数组

        参数:
            n: 树状数组的大小（处理的元素范围为1..n）
        """
        # mx_length[i]：树状数组中第i个节点维护的区间内的最大长度
        self.mx_length = [0] * (n + 1)
        # mx_cnt[i]：树状数组中第i个节点维护的区间内，对应最大长度的计数
        self.mx_cnt = [0] * (n + 1)

    def lowbit(self, i):
        """
        计算i的最低位1对应的数值（树状数组索引计算的核心）

        参数:
            i: 输入的整数

        返回:
            i的二进制表示中最低位1所对应的值（如6(110)的lowbit为2(10)）
        """
        return i & -i

    def add(self, i: int, length: int, cnt: int):
        """
        单点更新：更新位置i对应的长度和计数，维护树状数组中相关区间的最大长度及计数

        对于树状数组中以i为起点的所有相关节点（通过lowbit扩展），更新其维护的最大长度：
        - 若节点当前最大长度等于输入length，则累加计数
        - 若节点当前最大长度小于输入length，则更新最大长度为输入length，并重置计数为输入cnt
        - 若节点当前最大长度大于输入length，则不做处理

        参数:
            i: 要更新的位置（1-based索引）
            length: 待更新的长度值
            cnt: 该长度对应的计数（出现次数）
        """
        # 沿树状数组的索引链向上更新（i += lowbit(i)）
        while i < len(self.mx_length):
            if self.mx_length[i] == length:
                # 长度相等，累加计数
                self.mx_cnt[i] += cnt
            elif self.mx_length[i] < length:
                # 新长度更大，更新最大长度和计数
                self.mx_cnt[i] = cnt
                self.mx_length[i] = length
            # 若新长度更小，不更新
            i += self.lowbit(i)

    def sum(self, i: int):
        """
        前缀查询：查询1到i范围内的最大长度，以及该长度的总计数

        遍历树状数组中与i相关的所有节点（通过lowbit收缩），聚合得到前缀范围内的最大长度及总计数：
        - 若当前记录的最大长度等于节点的最大长度，累加计数
        - 若当前记录的最大长度小于节点的最大长度，更新最大长度为节点的长度，并重置计数为节点的计数
        - 若当前记录的最大长度大于节点的最大长度，不做处理

        参数:
            i: 前缀的结束位置（1-based索引）

        返回:
            元组 (max_length, total_cnt)，其中：
            - max_length: 1到i范围内的最大长度
            - total_cnt: 该最大长度在1到i范围内的总计数
        """
        length = cnt = 0  # 初始化最大长度和计数
        # 沿树状数组的索引链向下查询（i -= lowbit(i)）
        while i > 0:
            if length == self.mx_length[i]:
                # 长度相等，累加计数
                cnt += self.mx_cnt[i]
            elif length < self.mx_length[i]:
                # 发现更大的长度，更新长度和计数
                cnt = self.mx_cnt[i]
                length = self.mx_length[i]
            # 若当前长度更大，不更新
            i -= self.lowbit(i)
        return length, cnt


class BIT:
    """
    维护前缀范围内最大长度及其计数的树状数组（Binary Indexed Tree变种）

    该数据结构用于高效管理元素的长度信息，支持两种核心操作：
    1. 查询前缀[1..i]中的最大长度及该长度的总计数
    2. 更新位置i的长度信息，维护相关区间的最大长度和计数
    适用于需要动态追踪最大长度并统计其出现次数的场景（如序列分析、动态规划优化等）
    """

    def __init__(self, n):
        """
        初始化树状数组

        参数:
            n: 树状数组的大小（索引范围通常为1..n-1，因内部数组长度为n）
        """
        self.len = [0] * n  # 存储每个树状数组节点维护的区间内的最大长度
        self.cnt = [0] * n  # 存储对应最大长度的计数（出现次数）
        self.n = n  # 树状数组的总大小

    def query(self, i):
        """
        查询前缀[1..i]范围内的最大长度及其总计数

        遍历树状数组中与i相关的节点（通过i -= i & -i收缩范围），聚合得到：
        - 前缀中的最大长度
        - 该最大长度在 prefix 范围内的总出现次数

        参数:
            i: 前缀的结束位置（1-based索引）

        返回:
            元组 (max_length, total_count)，其中：
            - max_length: 前缀[1..i]中的最大长度
            - total_count: 该最大长度在 prefix 范围内的总计数
        """
        l, c = 0, 0  # 初始化最大长度为0，计数为0
        while i > 0:
            if self.len[i] > l:
                # 发现更大的长度，更新最大长度和计数
                l = self.len[i]
                c = self.cnt[i]
            elif self.len[i] == l:
                # 长度相等，累加计数
                c += self.cnt[i]
            # 移动到下一个相关节点（通过lowbit收缩）
            i -= i & -i
        return l, c

    def update(self, i, l, c):
        """
        更新位置i的长度信息，维护树状数组相关区间的最大长度和计数

        遍历树状数组中以i为起点的相关节点（通过i += i & -i扩展范围），更新规则：
        - 若节点当前最大长度小于l，则更新为l并重置计数为c
        - 若节点当前最大长度等于l，则累加计数c
        - 若节点当前最大长度大于l，则不做处理

        参数:
            i: 要更新的位置（1-based索引）
            l: 待更新的长度值
            c: 该长度对应的计数（出现次数）
        """
        while i < self.n:
            if self.len[i] < l:
                # 新长度更大，更新最大长度和计数
                self.len[i] = l
                self.cnt[i] = c
            elif self.len[i] == l:
                # 长度相等，累加计数
                self.cnt[i] += c
            # 移动到下一个相关节点（通过lowbit扩展）
            i += i & -i