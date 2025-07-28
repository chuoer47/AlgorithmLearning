class SegmentTree:
    """
    线段树（Segment Tree）实现，支持单点修改和区间求和查询

    线段树是一种高效处理区间查询和单点更新的数据结构，
    时间复杂度均为O(log n)，适用于需要频繁进行这两种操作的场景。
    """

    def __init__(self, data: list):
        """
        初始化线段树

        参数:
            data: 初始数据列表（0-based索引）
        """
        self.n = len(data)  # 原始数据长度
        self.size = 1  # 线段树大小（取大于等于n的最小2的幂）
        while self.size < self.n:
            self.size <<= 1  # 等价于self.size *= 2

        # 线段树数组，大小为2*size，其中[0, size)为叶子节点，[size, 2*size)为内部节点
        self.tree = [0] * (2 * self.size)

        # 初始化叶子节点
        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        # 构建内部节点（从最后一个非叶子节点向前构建）
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos: int, value: int) -> None:
        """
        单点修改：将原始数据中pos位置的值更新为value

        参数:
            pos: 原始数据中的位置（0-based索引）
            value: 新值
        """
        # 转换为线段树叶子节点索引
        pos += self.size

        # 更新叶子节点值
        self.tree[pos] = value

        # 向上更新父节点
        pos >>= 1  # 等价于pos = pos // 2
        while pos >= 1:
            # 当前节点值 = 左子节点值 + 右子节点值
            new_val = self.tree[2 * pos] + self.tree[2 * pos + 1]
            if self.tree[pos] == new_val:
                break  # 若值未变化，提前终止更新
            self.tree[pos] = new_val
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        """
        区间查询：计算原始数据中[l, r)区间的元素和（左闭右开）

        参数:
            l: 区间左端点（0-based索引，包含）
            r: 区间右端点（0-based索引，不包含）

        返回:
            区间[l, r)的元素和
        """
        res = 0
        l += self.size  # 转换为线段树叶子节点索引
        r += self.size

        # 遍历左右区间，累加结果
        while l < r:
            # 若左端点是右孩子，直接累加并移动到下一个区间
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            # 若右端点是右孩子，累加其左兄弟并移动到上一个区间
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            # 向上移动一层
            l >>= 1
            r >>= 1
        return res


# 使用示例
if __name__ == "__main__":
    # 初始化数据
    data = [1, 3, 5, 7, 9, 11]
    print(f"初始数据: {data}")

    # 创建线段树
    st = SegmentTree(data)

    # 测试区间查询
    print(f"查询[0, 3)的和: {st.query(0, 3)}")  # 1+3+5=9
    print(f"查询[2, 5)的和: {st.query(2, 5)}")  # 5+7+9=21
    print(f"查询[0, 6)的和: {st.query(0, 6)}")  # 1+3+5+7+9+11=36

    # 测试单点修改：将索引2的值从5改为10
    st.update(2, 10)
    print("\n修改后数据: [1, 3, 10, 7, 9, 11]")

    # 再次查询验证
    print(f"查询[0, 3)的和: {st.query(0, 3)}")  # 1+3+10=14
    print(f"查询[2, 5)的和: {st.query(2, 5)}")  # 10+7+9=26
    print(f"查询[0, 6)的和: {st.query(0, 6)}")  # 1+3+10+7+9+11=41

    # 再修改一个值：将索引5的值从11改为20
    st.update(5, 20)
    print("\n再次修改后数据: [1, 3, 10, 7, 9, 20]")
    print(f"查询[0, 6)的和: {st.query(0, 6)}")  # 1+3+10+7+9+20=50
