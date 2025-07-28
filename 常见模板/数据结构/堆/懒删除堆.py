from collections import defaultdict
from heapq import *


class LazyHeap:
    """
    带懒删除功能的堆（优先队列）实现

    懒删除机制：不立即从堆中物理删除元素，而是通过记录待删除元素的次数，
    在访问堆顶元素时再清理无效元素，从而优化删除操作的时间复杂度。
    适用于需要频繁插入、删除和访问最小值的场景。
    """

    def __init__(self):
        self.heap = []  # 底层存储元素的堆（最小堆）
        self.remove_cnt = defaultdict(int)  # 记录每个元素待删除的次数
        self.size = 0  # 堆中有效元素的实际数量

    def remove(self, x: int) -> None:
        """
        懒删除指定元素x

        不直接从堆中移除x，而是增加其待删除计数，延迟到访问堆顶时处理。
        注意：调用此方法前需确保x存在于堆中（或至少曾经存在）。

        参数:
            x: 需要删除的元素
        """
        self.remove_cnt[x] += 1  # 增加待删除计数
        self.size -= 1  # 有效元素数量减1

    def apply_remove(self) -> None:
        """
        清理堆顶的无效元素

        当堆顶元素存在待删除计数时，将其从堆中物理删除并减少计数，
        重复此过程直到堆顶元素为有效元素（无待删除计数）或堆为空。
        """
        # 循环检查堆顶，处理所有待删除的元素
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1  # 减少待删除计数
            heappop(self.heap)  # 从堆中移除该元素

    def top(self) -> int:
        """
        获取堆顶元素（最小值）

        先清理堆顶无效元素，再返回当前堆顶的有效元素。

        返回:
            堆中的最小元素
        """
        self.apply_remove()  # 确保堆顶有效
        return self.heap[0]

    def pop(self) -> int:
        """
        弹出并返回堆顶元素（最小值）

        先清理堆顶无效元素，再弹出堆顶并更新有效元素数量。

        返回:
            堆中的最小元素
        """
        self.apply_remove()  # 确保堆顶有效
        self.size -= 1  # 有效元素数量减1
        return heappop(self.heap)

    def push(self, x: int) -> None:
        """
        向堆中插入元素x

        若x存在待删除计数，则通过减少计数抵消一次删除；
        否则直接将x插入堆中。最后更新有效元素数量。

        参数:
            x: 需要插入的元素
        """
        if self.remove_cnt[x] > 0:
            # 若x有未处理的删除，优先抵消
            self.remove_cnt[x] -= 1
        else:
            # 否则直接入堆
            heappush(self.heap, x)
        self.size += 1  # 有效元素数量加1

    def pushpop(self, x: int) -> int:
        """
        插入元素x后，立即弹出并返回当前堆顶元素（最小值）

        先清理堆顶无效元素，再执行插入+弹出操作，等价于push(x)后pop()，
        但比单独调用更高效。

        参数:
            x: 需要插入的元素

        返回:
            操作后堆中的最小元素
        """
        self.apply_remove()  # 确保堆顶有效
        return heappushpop(self.heap, x)