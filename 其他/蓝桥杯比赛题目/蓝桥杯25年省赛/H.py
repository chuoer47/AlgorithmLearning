from cmath import inf
from heapq import *

# 反悔堆，没什么难度
n, m, o = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]


class Heap:
    def __init__(self):
        self.hq = []
        self.fee = 0

    def push(self, nums):
        x, y = nums
        self.fee += -x * y
        heappush(self.hq, nums)

    def pop(self):
        x, y = heappop(self.hq)
        self.fee -= -x * y
        return x, y


def solution(m, o, graph):
    if sum(b for a, b, c in graph) < m:
        # 装不满的特殊情况
        return -1
    hq = Heap()
    size = 0
    ans = inf
    for price, stock, fee in graph:
        dis_cost = fee * o
        if size < m:
            # 先把货车塞满
            pre = stock
            stock = min(stock, m - size)
            hq.push((-price, stock))
            size += stock
            stock = pre - stock
        # print("---", price, size, stock)
        if size == m:
            # 装满货车后需要减少
            while stock > 0 and hq and -hq.hq[0][0] > price:
                pmx, pstock = hq.pop()
                pmx = -pmx
                if pstock <= stock:
                    # 全部替换
                    stock -= pstock
                    hq.push((-price, pstock))
                elif pstock > stock:
                    # stock消费完也替换不了，能替换多少替换多少
                    hq.push((-pmx, pstock - stock))
                    hq.push((-price, stock))
                    stock = 0

            # print(hq.fee + dis_cost)
            ans = min(ans, hq.fee + dis_cost)
    return ans if ans != inf else -1


try:
    if n <= 5000 and m <= 50000:
        ans = solution(m, o, graph)
        print(ans)
    elif m <= 50000:
        ans = solution(m, o, graph)
        print(ans)
    else:
        ans = solution(m, o, graph)
        print(ans)
except:
    print(-1)
