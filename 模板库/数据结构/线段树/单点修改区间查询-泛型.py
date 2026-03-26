from typing import List, Callable, TypeVar

# 定义泛型类型，支持任意可比较/可合并的数据类型
T = TypeVar('T')


class GenericSegmentTree:
    """
    泛型线段树，支持自定义合并操作（如求和、最大值、最小值等）

    通过传入合并函数和中性元素，可适配不同的区间查询需求，实现"泛型"效果。
    """

    def __init__(
            self,
            data: List[T],
            merge_func: Callable[[T, T], T],
            neutral: T
    ):
        """
        初始化泛型线段树

        参数:
            data: 初始数据列表（0-based索引）
            merge_func: 合并函数，用于计算父节点值（如sum: lambda a,b: a+b；max: lambda a,b: max(a,b)）
            neutral: 中性元素（合并操作的单位元，如求和为0，求最大值为-∞）
        """
        self.n = len(data)
        self.merge = merge_func  # 合并函数
        self.neutral = neutral  # 中性元素

        # 计算线段树大小（取大于等于n的最小2的幂）
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # 初始化线段树数组，用中性元素填充
        self.tree = [neutral] * (2 * self.size)

        # 填充叶子节点
        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        # 构建内部节点（从最后一个非叶子节点向前计算）
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos: int, value: T) -> None:
        """
        单点修改：将原始数据中pos位置的值更新为value

        参数:
            pos: 原始数据中的位置（0-based索引）
            value: 新值（类型需与初始化时的数据一致）
        """
        pos += self.size  # 转换为叶子节点索引
        self.tree[pos] = value

        # 向上更新父节点
        pos >>= 1  # 等价于pos = pos // 2
        while pos >= 1:
            new_val = self.merge(self.tree[2 * pos], self.tree[2 * pos + 1])
            if self.tree[pos] == new_val:
                break  # 若值未变化，提前终止
            self.tree[pos] = new_val
            pos >>= 1

    def query(self, l: int, r: int) -> T:
        """
        区间查询：计算[l, r)区间的合并结果（左闭右开）

        参数:
            l: 区间左端点（0-based索引，包含）
            r: 区间右端点（0-based索引，不包含）

        返回:
            区间[l, r)的合并结果（类型与初始化时的数据一致）
        """
        res = self.neutral  # 初始化为中性元素
        l += self.size
        r += self.size

        while l < r:
            if l % 2 == 1:
                # 左端点是右孩子，直接合并并移动
                res = self.merge(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                # 右端点是右孩子，合并左兄弟并移动
                r -= 1
                res = self.merge(res, self.tree[r])
            # 向上移动一层
            l >>= 1
            r >>= 1
        return res


# ------------------------------
# 示例1：区间求和线段树
# ------------------------------
if __name__ == "__main__":
    print("=== 区间求和示例 ===")
    data_sum = [1, 3, 5, 7, 9, 11]
    # 初始化求和线段树（合并函数为加法，中性元素为0）
    st_sum = GenericSegmentTree(
        data=data_sum,
        merge_func=lambda a, b: a + b,
        neutral=0
    )
    print(f"初始数据: {data_sum}")
    print(f"查询[0, 3)的和: {st_sum.query(0, 3)}")  # 1+3+5=9
    st_sum.update(2, 10)  # 将索引2的值从5改为10
    print(f"修改后[0, 3)的和: {st_sum.query(0, 3)}")  # 1+3+10=14

    # ------------------------------
    # 示例2：区间最大值线段树
    # ------------------------------
    print("\n=== 区间最大值示例 ===")
    data_max = [1, 3, 5, 7, 9, 11]
    # 初始化最大值线段树（合并函数为max，中性元素为-∞）
    st_max = GenericSegmentTree(
        data=data_max,
        merge_func=lambda a, b: max(a, b),
        neutral=-float('inf')
    )
    print(f"初始数据: {data_max}")
    print(f"查询[0, 4)的最大值: {st_max.query(0, 4)}")  # max(1,3,5,7)=7
    st_max.update(3, 2)  # 将索引3的值从7改为2
    print(f"修改后[0, 4)的最大值: {st_max.query(0, 4)}")  # max(1,3,5,2)=5

    # ------------------------------
    # 示例3：区间最小值线段树
    # ------------------------------
    print("\n=== 区间最小值示例 ===")
    data_min = [1, 3, 5, 7, 9, 11]
    # 初始化最小值线段树（合并函数为min，中性元素为+∞）
    st_min = GenericSegmentTree(
        data=data_min,
        merge_func=lambda a, b: min(a, b),
        neutral=float('inf')
    )
    print(f"初始数据: {data_min}")
    print(f"查询[2, 6)的最小值: {st_min.query(2, 6)}")  # min(5,7,9,11)=5
    st_min.update(2, 15)  # 将索引2的值从5改为15
    print(f"修改后[2, 6)的最小值: {st_min.query(2, 6)}")  # min(15,7,9,11)=7
