from collections import Counter
from heapq import heappush, heappop


class DualHeap:
    """对顶堆，实时计算当前集合前k小的元素和(如果k设0,则保持平衡，0<=small-large<=1)。每个操作均摊时间复杂度O(lgn)，总体O(nlgn)。682ms"""

    def __init__(self, k=0):
        self.k = k  # 如果k=0，表示保持两个堆一样大（0<=small-large<=1），此时-small[0]就是中位数
        self.small = []  # 大顶堆存较小的k个数，注意py默认小顶堆，因此需要取反
        self.large = []  # 小顶堆存较大的剩余数
        self.delay_rm = Counter()  # 延时删除标记
        self.sum_kth = 0  # 前k小数字的和
        self.small_size = 0
        self.large_size = 0

    def prune(self, h):
        """修剪h，使h堆顶的已标记删除元素全部弹出"""
        delay_rm = self.delay_rm
        p = -1 if h is self.small else 1
        while h:
            v = h[0] * p
            if v in delay_rm:
                delay_rm[v] -= 1
                if not delay_rm[v]:
                    del delay_rm[v]
                heappop(h)
            else:
                break

    def make_balance(self):
        """调整small和large的大小，使small中达到k个（或清空large）"""
        k = self.k or (self.small_size + self.large_size + 1) // 2  # 如果self.k是0，表示前后要balance
        if self.small_size > k:
            heappush(self.large, -self.small[0])
            self.sum_kth += heappop(self.small)  # 其实是-=负数
            self.large_size += 1
            self.small_size -= 1
            self.prune(self.small)
        elif self.small_size < k and self.large:
            heappush(self.small, -self.large[0])
            self.sum_kth += heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def add(self, v):
        """添加值v，判断需要加到哪个堆"""
        small = self.small
        if not small or v <= -small[0]:
            heappush(small, -v)
            self.sum_kth += v
            self.small_size += 1
        else:
            heappush(self.large, v)
            self.large_size += 1
        self.make_balance()

    def remove(self, v):
        """移除v，延时删除，但可以实时判断是否贡献了前k和"""
        small, large = self.small, self.large
        self.delay_rm[v] += 1
        if large and v >= large[0]:
            self.large_size -= 1
            if v == large[0]:
                self.prune(large)
        else:
            self.small_size -= 1
            self.sum_kth -= v
            if v == -small[0]:
                self.prune(small)
        self.make_balance()
