class Node:
    """线段树节点类，用于动态开点"""
    __slots__ = ['left', 'right', 'val']

    def __init__(self, val):
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        self.val = val  # 当前节点存储的值


class DynamicSegmentTree:
    """
    动态开点线段树（单点修改+区间查询）

    通过传入自定义合并函数实现多用途查询（求和/最大值/最小值等）
    """

    def __init__(self, merge_func, neutral_val, min_range=-10 ** 18, max_range=10 ** 18):
        """
        初始化线段树

        参数:
            merge_func: 合并函数，接收两个参数返回合并结果（如sum: lambda a,b: a+b）
            neutral_val: 中性值（合并操作的单位元，如求和为0，最大值为-∞）
            min_range: 支持的最小值域
            max_range: 支持的最大值域
        """
        self.merge = merge_func  # 合并左右子树的函数
        self.neutral = neutral_val  # 中性值
        self.min_r = min_range  # 值域下界
        self.max_r = max_range  # 值域上界
        self.root = Node(neutral_val)  # 根节点

    def _update(self, node, l, r, pos, value):
        """递归执行单点更新"""
        if l == r:
            node.val = value
            return

        mid = (l + r) // 2
        # 动态创建左子节点
        if pos <= mid:
            if not node.left:
                node.left = Node(self.neutral)
            self._update(node.left, l, mid, pos, value)
        # 动态创建右子节点
        else:
            if not node.right:
                node.right = Node(self.neutral)
            self._update(node.right, mid + 1, r, pos, value)

        # 合并左右子节点的值
        left_val = node.left.val if node.left else self.neutral
        right_val = node.right.val if node.right else self.neutral
        node.val = self.merge(left_val, right_val)

    def update(self, pos, value):
        """
        单点修改：将pos位置的值设为value

        参数:
            pos: 要修改的位置（需在[min_range, max_range]范围内）
            value: 新值
        """
        if not (self.min_r <= pos <= self.max_r):
            raise ValueError(f"位置{pos}超出值域范围")
        self._update(self.root, self.min_r, self.max_r, pos, value)

    def _query(self, node, l, r, ql, qr):
        """递归执行区间查询"""
        if not node or r < ql or l > qr:
            return self.neutral

        if ql <= l and r <= qr:
            return node.val

        mid = (l + r) // 2
        left_val = self._query(node.left, l, mid, ql, qr)
        right_val = self._query(node.right, mid + 1, r, ql, qr)

        return self.merge(left_val, right_val)

    def query(self, l, r):
        """
        区间查询：计算[l, r]区间的合并结果

        参数:
            l: 查询区间左端点
            r: 查询区间右端点

        返回:
            区间合并结果
        """
        if l > r:
            return self.neutral
        # 限制查询范围在支持的值域内
        ql = max(l, self.min_r)
        qr = min(r, self.max_r)
        return self._query(self.root, self.min_r, self.max_r, ql, qr)


# ------------------------------
# 使用示例
# ------------------------------
if __name__ == "__main__":
    # 示例1：区间求和
    print("=== 区间求和示例 ===")
    # 合并函数：加法；中性值：0
    sum_st = DynamicSegmentTree(
        merge_func=lambda a, b: a + b,
        neutral_val=0
    )
    sum_st.update(10, 5)  # 位置10的值设为5
    sum_st.update(20, 3)  # 位置20的值设为3
    sum_st.update(30, 7)  # 位置30的值设为7
    print(f"查询[5, 25]的和：{sum_st.query(5, 25)}")  # 5+3=8
    print(f"查询[0, 100]的和：{sum_st.query(0, 100)}")  # 5+3+7=15

    # 示例2：区间最大值
    print("\n=== 区间最大值示例 ===")
    # 合并函数：取最大值；中性值：负无穷
    max_st = DynamicSegmentTree(
        merge_func=lambda a, b: max(a, b),
        neutral_val=-float('inf')
    )
    max_st.update(5, 10)
    max_st.update(15, 20)
    max_st.update(25, 15)
    print(f"查询[10, 20]的最大值：{max_st.query(10, 20)}")  # 20
    print(f"查询[0, 30]的最大值：{max_st.query(0, 30)}")  # 20

    # 示例3：区间最小值
    print("\n=== 区间最小值示例 ===")
    # 合并函数：取最小值；中性值：正无穷
    min_st = DynamicSegmentTree(
        merge_func=lambda a, b: min(a, b),
        neutral_val=float('inf')
    )
    min_st.update(5, 10)
    min_st.update(15, 20)
    min_st.update(25, 15)
    print(f"查询[10, 20]的最小值：{min_st.query(10, 20)}")  # 20
    print(f"查询[0, 30]的最小值：{min_st.query(0, 30)}")  # 10
