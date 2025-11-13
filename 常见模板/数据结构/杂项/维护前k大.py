
from sortedcontainers import SortedList


class TopKMaintainer:
    def __init__(self, k: int):
        """初始化前k个最大值维护器"""
        if k < 0:
            raise ValueError("k必须为非负整数")
        self.k = k
        self.upper = SortedList()  # 存储前k个最大值（升序，最小元素在首位）
        self.lower = SortedList()  # 存储剩余元素（升序，最大元素在末尾）

    def add(self, x: int) -> None:
        """添加元素并动态维护前k个最大值"""
        if len(self.upper) < self.k:
            # upper未满，直接加入
            self.upper.add(x)
        else:
            # upper已满，判断是否替换
            if self.k == 0:
                # k=0时，所有元素都放入lower
                self.lower.add(x)
                return
            # 新元素大于upper的最小值，需要替换
            if x > self.upper[0]:
                removed = self.upper.pop(0)  # 移除upper中最小的元素
                self.lower.add(removed)  # 移至lower
                self.upper.add(x)  # 加入新元素
            else:
                self.lower.add(x)

    def remove(self, x: int) -> None:
        """删除元素并动态维护前k个最大值"""
        if x in self.upper:
            # 从upper删除后，尝试从lower取最大元素补充
            self.upper.remove(x)
            if self.lower:  # 若lower非空，取最大元素补充至upper
                max_lower = self.lower.pop()  # lower是升序，末尾为最大
                self.upper.add(max_lower)
        elif x in self.lower:
            # 从lower直接删除
            self.lower.remove(x)
        else:
            raise ValueError(f"元素{x}不存在于当前集合中")

    def get_top_k(self, descending: bool = False) -> list:
        """获取前k个最大值（默认升序，descending=True时返回降序）"""
        if descending:
            return list(reversed(self.upper))
        return list(self.upper)

    def __str__(self) -> str:
        """打印当前状态"""
        return f"前{self.k}个最大值: {self.get_top_k()}, 剩余元素: {list(self.lower)}"