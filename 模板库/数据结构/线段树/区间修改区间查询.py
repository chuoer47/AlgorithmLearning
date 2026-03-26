from typing import List


class SegmentTree:
    """
    支持区间修改（区间加法）和区间查询（区间求和）的线段树

    采用懒标记（Lazy Propagation）技术优化区间修改，将区间修改和查询的时间复杂度
    均保持在O(log n)，适用于需要频繁进行范围更新和范围统计的场景。
    """

    def __init__(self, data: List[int]):
        """
        初始化线段树

        参数:
            data: 初始数据列表（0-based索引）
        """
        self.n = len(data)  # 原始数据长度
        self.size = 1  # 线段树大小（取大于等于n的最小2的幂）
        while self.size < self.n:
            self.size <<= 1

        # 线段树数组：存储区间和
        self.tree = [0] * (2 * self.size)
        # 懒标记数组：存储待传递的区间增量
        self.lazy = [0] * (2 * self.size)

        # 初始化叶子节点
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # 构建内部节点
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def _push_down(self, node: int, l: int, r: int) -> None:
        """
        懒标记下推：将当前节点的待更新增量传递给子节点

        参数:
            node: 当前节点索引
            l: 当前节点覆盖的区间左端点
            r: 当前节点覆盖的区间右端点
        """
        if self.lazy[node] == 0:
            return  # 无待更新增量，直接返回

        mid = (l + r) // 2
        left = 2 * node  # 左子节点索引
        right_node = 2 * node + 1  # 右子节点索引

        # 左子节点：区间长度为(mid - l + 1)
        self.tree[left] += self.lazy[node] * (mid - l + 1)
        self.lazy[left] += self.lazy[node]

        # 右子节点：区间长度为(r - mid)
        self.tree[right_node] += self.lazy[node] * (r - mid)
        self.lazy[right_node] += self.lazy[node]

        # 清空当前节点的懒标记
        self.lazy[node] = 0

    def _update_range(self, node: int, l: int, r: int, ul: int, ur: int, val: int) -> None:
        """
        递归实现区间更新（内部方法）

        参数:
            node: 当前节点索引
            l: 当前节点覆盖的区间左端点
            r: 当前节点覆盖的区间右端点
            ul: 待更新区间的左端点
            ur: 待更新区间的右端点
            val: 要增加的增量值
        """
        # 当前节点区间完全在更新区间内
        if ul <= l and r <= ur:
            self.tree[node] += val * (r - l + 1)  # 更新当前节点的区间和
            self.lazy[node] += val  # 标记待下推的增量
            return

        # 下推懒标记（确保子节点数据正确）
        self._push_down(node, l, r)
        mid = (l + r) // 2

        # 递归更新左子树
        if ul <= mid:
            self._update_range(2 * node, l, mid, ul, ur, val)
        # 递归更新右子树
        if ur > mid:
            self._update_range(2 * node + 1, mid + 1, r, ul, ur, val)

        # 更新当前节点的区间和（由子节点合并而来）
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update_range(self, l: int, r: int, val: int) -> None:
        """
        区间更新：给区间[l, r]（闭区间）的每个元素增加val

        参数:
            l: 待更新区间的左端点（0-based索引）
            r: 待更新区间的右端点（0-based索引）
            val: 要增加的增量值
        """
        self._update_range(1, 0, self.size - 1, l, r, val)

    def _query_range(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        """
        递归实现区间查询（内部方法）

        参数:
            node: 当前节点索引
            l: 当前节点覆盖的区间左端点
            r: 当前节点覆盖的区间右端点
            ql: 查询区间的左端点
            qr: 查询区间的右端点

        返回:
            区间[ql, qr]的和
        """
        # 当前节点区间完全在查询区间内
        if ql <= l and r <= qr:
            return self.tree[node]

        # 下推懒标记（确保子节点数据正确）
        self._push_down(node, l, r)
        mid = (l + r) // 2
        res = 0

        # 查询左子树
        if ql <= mid:
            res += self._query_range(2 * node, l, mid, ql, qr)
        # 查询右子树
        if qr > mid:
            res += self._query_range(2 * node + 1, mid + 1, r, ql, qr)

        return res

    def query_range(self, l: int, r: int) -> int:
        """
        区间查询：计算区间[l, r]（闭区间）的元素和

        参数:
            l: 查询区间的左端点（0-based索引）
            r: 查询区间的右端点（0-based索引）

        返回:
            区间[l, r]的元素和
        """
        return self._query_range(1, 0, self.size - 1, l, r)


# 使用示例
if __name__ == "__main__":
    # 初始化数据
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"初始数据: {data}")

    # 创建线段树
    st = SegmentTree(data)

    # 测试初始查询
    print(f"查询[0, 7]的和: {st.query_range(0, 7)}")  # 36
    print(f"查询[2, 5]的和: {st.query_range(2, 5)}")  # 3+4+5+6=18

    # 区间修改1：给[1, 3]的每个元素加3
    st.update_range(1, 3, 3)
    print("\n执行操作：[1,3]每个元素加3后")
    # 数据变为：[1, 5, 6, 7, 5, 6, 7, 8]
    print(f"查询[0, 7]的和: {st.query_range(0, 7)}")  # 36 + 3*3=45
    print(f"查询[1, 3]的和: {st.query_range(1, 3)}")  # 5+6+7=18

    # 区间修改2：给[4, 6]的每个元素减2
    st.update_range(4, 6, -2)
    print("\n执行操作：[4,6]每个元素减2后")
    # 数据变为：[1, 5, 6, 7, 3, 4, 5, 8]
    print(f"查询[4, 6]的和: {st.query_range(4, 6)}")  # 3+4+5=12
    print(f"查询[0, 7]的和: {st.query_range(0, 7)}")  # 45 - 2*3=39

    # 区间修改3：给[0, 7]的每个元素加1
    st.update_range(0, 7, 1)
    print("\n执行操作：[0,7]每个元素加1后")
    # 数据变为：[2, 6, 7, 8, 4, 5, 6, 9]
    print(f"查询[0, 7]的和: {st.query_range(0, 7)}")  # 39 + 8*1=47
