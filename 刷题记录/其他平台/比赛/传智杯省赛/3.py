from collections import deque, defaultdict
from heapq import *


# 方法1：
# 懒删除堆 + 对顶堆 => 长度=m
# 题目要求任意长度>=m的连续子数组
# 暴力遍历会超时，需要分析 >m 的连续子数组的性质？
# 假设暴力从 [m,n] 使用对顶堆完成，需要的时间是 n*logn*n X(超时)
# 我们假设左指针指的数如果既满足在下面的堆，又满足去除后长度依旧在 >=m.这种贪心能否满足题目条件
# 感觉贪心没有考虑到很多情况

# 方法2：贡献法
# 可以先判断每个元素能否成为中位数，找到可以为中位数的最大值
# 如何判断每个元素能否成为中位数？
# x1 x2 x3 x4 x5 .... xn
# 假设 xi 能成为中位数 => 要么出现在>=m的奇数长度的的中间，要么出现在偶数长度的下中位数
# 出现在>=m的奇数长度的的中间，l个>=xi,l个<=xi,加起来 2*l + 1的窗口
# 不可行，有问题....情况难以考虑完全，而且不知道如何高效判断

# 有什么情况是考虑长度 >m 反而能获得更大的中位数的情况
#

# ========== 下面开始尝试方法1
class LazyHeap:
    def __init__(self):
        self.hq = []
        self.size = 0
        self.cnt = defaultdict(int)  # 计算当前堆里面有的元素的数量
        self.lazy = defaultdict(int)  # 保存当前懒删除的元素

    def add(self, x):
        heappush(self.hq, x)
        self.cnt[x] += 1
        self.size += 1

    def delete(self, x):
        self.cnt[x] -= 1
        self.lazy[x] += 1
        self.size -= 1

    def pop(self):
        while self.hq and self.lazy[self.hq[0]] > 0:
            self.lazy[heappop(self.hq)] -= 1
        x = heappop(self.hq)
        self.cnt[x] -= 1
        self.size -= 1
        return x

    def top(self):
        while self.hq and self.lazy[self.hq[0]] > 0:
            self.lazy[heappop(self.hq)] -= 1
        return self.hq[0]

    def isEmpty(self):
        return self.size == 0

# 1
def helper(n, m, nums):
    ans = 0
    # 维护两个对顶堆
    upper = LazyHeap()  # 维护的是最小堆
    lower = LazyHeap()  # 维护的是最大堆
    # upper[0] >= -lower[0]
    # 时刻维护 size(upper) + 1 = size(lower)[奇数] or size(upper) = size(lower)[偶数]
    l = 0
    for r, v in enumerate(nums):
        # 把v加入对顶堆 + 维护对顶堆

        upper.add(v)
        while not upper.isEmpty() and not lower.isEmpty() and upper.top() < -lower.top():
            x = upper.pop()
            y = -lower.pop()
            upper.add(y)
            lower.add(-x)
        while upper.size > lower.size:
            x = upper.pop()
            lower.add(-x)
        if r - l + 1 < m:  # 长度还没有到 m
            continue
        ans = max(ans, -lower.top())
        while lower.cnt[-nums[l]] > 0 and r - l + 1 > m:
            lower.delete(-nums[l])  # 懒删除
            while not upper.isEmpty() and not lower.isEmpty() and upper.top() < -lower.top():
                x = upper.pop()
                y = -lower.pop()
                upper.add(y)
                lower.add(-x)
            while upper.size > lower.size:
                x = upper.pop()
                lower.add(-x)
            ans = max(ans, -lower.top())

    return ans


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(helper(n, m, nums))
