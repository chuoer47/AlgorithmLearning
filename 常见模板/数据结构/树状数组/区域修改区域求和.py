class FenwickTree:
    """
    支持区间修改与区间求和的树状数组（Fenwick Tree）实现

    基于差分思想，通过维护两个树状数组实现高效的区间更新（对[l, r]加val）和区间求和（计算[l, r]的和），
    所有操作的时间复杂度均为O(log n)，适用于需要频繁进行区间增减和区间总和查询的场景。
    """

    def __init__(self, n: int):
        """
        初始化树状数组

        参数:
            n: 数组的大小（处理的元素范围为1..n）
        """
        self.n = n  # 数组大小
        # tree数组：维护差分数组d[i]的树状数组，其中d[i] = a[i] - a[i-1]（a[0] = 0）
        self.tree = [0] * (n + 1)
        # itree数组：维护i*d[i]的树状数组，用于推导区间和公式
        self.itree = [0] * (n + 1)

    def update(self, x: int, delta: int):
        """
        对tree数组进行单点更新（针对差分数组d[x]）

        用于更新差分数组d[x]，增加delta，是树状数组的标准单点更新操作。

        参数:
            x: 要更新的位置（1-based索引）
            delta: 增加的值
        """
        while x <= self.n:
            self.tree[x] += delta
            x += x & -x  # 基于lowbit更新下一个节点

    def iupdate(self, i: int, val: int):
        """
        对itree数组进行单点更新（针对i*d[i]）

        用于更新i*d[i]的值，增加val，配合tree数组实现区间和计算。

        参数:
            i: 要更新的位置（1-based索引）
            val: 增加的值
        """
        while i <= self.n:
            self.itree[i] += val
            i += i & -i  # 基于lowbit更新下一个节点

    def add(self, x: int, val: int):
        """
        对差分数组进行操作，实现从x到n的区间增加val（单边区间更新）

        原理：通过在差分数组d[x]增加val，等价于对原数组[x, n]区间的每个元素加val。
        内部通过更新tree（d[x] += val）和itree（i*d[x] += x*val）实现。

        参数:
            x: 区间的起始位置（1-based索引）
            val: 要增加的值
        """
        self.update(x, val)  # d[x] += val
        self.iupdate(x, x * val)  # i*d[x] 对应位置增加 x*val

    def rangeAdd(self, l: int, r: int, val: int):
        """
        实现对[l, r]区间的每个元素增加val（区间修改）

        基于差分思想：对原数组[l, r]加val，等价于在差分数组d[l] += val，d[r+1] -= val。
        通过两次add操作实现：add(l, val)和add(r+1, -val)。

        参数:
            l: 区间起始位置（1-based索引）
            r: 区间结束位置（1-based索引）
            val: 要增加的值
        """
        self.add(l, val)  # 对[l, n]加val
        if r + 1 <= self.n:
            self.add(r + 1, -val)  # 对[r+1, n]减val，抵消超出r的部分

    def pre(self, i: int) -> int:
        """
        查询tree数组的前缀和，即d[1]到d[i]的和

        用于计算差分数组d的前缀和，是树状数组的标准前缀查询操作。

        参数:
            i: 前缀结束位置（1-based索引）

        返回:
            d[1] + d[2] + ... + d[i]
        """
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1  # 等价于i -= i & -i，移动到前一个节点
        return res

    def iper(self, i: int) -> int:
        """
        查询itree数组的前缀和，即1*d[1]到i*d[i]的和

        用于辅助计算原数组的前缀和，是树状数组的标准前缀查询操作。

        参数:
            i: 前缀结束位置（1-based索引）

        返回:
            1*d[1] + 2*d[2] + ... + i*d[i]
        """
        res = 0
        while i > 0:
            res += self.itree[i]
            i &= i - 1  # 移动到前一个节点
        return res

    def rangeX(self, x: int) -> int:
        """
        计算原数组[1, x]的前缀和（1到x的元素总和）

        公式推导：原数组前缀和sum(1..x) = sum_{k=1 to x} (sum_{i=1 to k} d[i])
        化简后为 (x+1)*pre(x) - iper(x)，其中pre(x)是d的前缀和，iper(x)是i*d[i]的前缀和。

        参数:
            x: 前缀结束位置（1-based索引）

        返回:
            原数组[1, x]的总和
        """
        a = self.pre(x)  # sum(d[1..x])
        b = self.iper(x)  # sum(i*d[i] for i=1..x)
        return (x + 1) * a - b

    def rangeQuery(self, l: int, r: int) -> int:
        """
        计算原数组[l, r]区间的总和（区间求和）

        原理：通过前缀和相减，[l, r]的和 = 前缀和(r) - 前缀和(l-1)。

        参数:
            l: 区间起始位置（1-based索引）
            r: 区间结束位置（1-based索引）

        返回:
            原数组[l, r]的总和
        """
        return self.rangeX(r) - self.rangeX(l - 1)


# 案例：动态数组的区间修改与查询
if __name__ == "__main__":
    # 初始化一个大小为5的FenwickTree（处理1~5索引的元素，初始数组全为0）
    size = 5
    ft = FenwickTree(size)
    print("初始数组（全为0）：")
    print(f"查询[1,5]的和：{ft.rangeQuery(1, 5)}")  # 预期：0

    # 操作1：给区间[1,3]的每个元素加2
    ft.rangeAdd(l=1, r=3, val=2)
    print("\n执行操作：给[1,3]加2后：")
    # 此时数组应为 [2, 2, 2, 0, 0]（索引1~5）
    print(f"查询[1,3]的和：{ft.rangeQuery(1, 3)}")  # 预期：2+2+2=6
    print(f"查询[1,5]的和：{ft.rangeQuery(1, 5)}")  # 预期：2+2+2+0+0=6

    # 操作2：给区间[2,4]的每个元素加3
    ft.rangeAdd(l=2, r=4, val=3)
    print("\n执行操作：给[2,4]加3后：")
    # 此时数组应为 [2, 2+3=5, 2+3=5, 0+3=3, 0]（索引1~5）
    print(f"查询[2,4]的和：{ft.rangeQuery(2, 4)}")  # 预期：5+5+3=13
    print(f"查询[1,5]的和：{ft.rangeQuery(1, 5)}")  # 预期：2+5+5+3+0=15

    # 操作3：给区间[5,5]的元素加10（单点修改，等价于区间[5,5]）
    ft.rangeAdd(l=5, r=5, val=10)
    print("\n执行操作：给[5,5]加10后：")
    # 此时数组应为 [2,5,5,3,10]（索引1~5）
    print(f"查询[5,5]的和：{ft.rangeQuery(5, 5)}")  # 预期：10
    print(f"查询[1,5]的和：{ft.rangeQuery(1, 5)}")  # 预期：2+5+5+3+10=25

    # 操作4：给区间[1,5]的每个元素减1
    ft.rangeAdd(l=1, r=5, val=-1)
    print("\n执行操作：给[1,5]减1后：")
    # 此时数组应为 [1,4,4,2,9]（索引1~5）
    print(f"查询[3,5]的和：{ft.rangeQuery(3, 5)}")  # 预期：4+2+9=15
    print(f"查询[1,5]的和：{ft.rangeQuery(1, 5)}")  # 预期：1+4+4+2+9=20
