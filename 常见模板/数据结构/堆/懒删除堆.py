from collections import defaultdict
from heapq import *


class LazyHeap:
    def __init__(self):
        self.heap = []
        self.remove_cnt = defaultdict(int)  # 每个元素剩余需要删除的次数
        self.size = 0  # 实际大小

    # 删除
    def remove(self, x: int) -> None:
        self.remove_cnt[x] += 1  # 懒删除
        self.size -= 1

    # 正式执行删除操作
    def apply_remove(self) -> None:
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heappop(self.heap)

    # 查看堆顶
    def top(self) -> int:
        self.apply_remove()
        return self.heap[0]

    # 出堆
    def pop(self) -> int:
        self.apply_remove()
        self.size -= 1
        return heappop(self.heap)

    # 入堆
    def push(self, x: int) -> None:
        if self.remove_cnt[x] > 0:
            self.remove_cnt[x] -= 1  # 抵消之前的删除
        else:
            heappush(self.heap, x)
        self.size += 1

    # push(x) 然后 pop()
    def pushpop(self, x: int) -> int:
        self.apply_remove()
        return heappushpop(self.heap, x)
