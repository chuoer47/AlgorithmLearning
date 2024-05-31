"""
https://www.acwing.com/problem/content/148/
这道题的思路如下：
1. 首先，将第一个录入的数组作为初始
2. 然后，将剩下m-1个录入的数组与前面的进行归并
3. 注意：每次归并仅取前n个
"""
from math import inf
from heapq import heappush, heappop


def merge(a, b):
    """
    合并a,b数组，取前n个最小的
    """
    c = []
    heap = []
    for i in range(n):
        heappush(heap, (b[i] + a[0], 0))
    for i in range(0, n):
        v, index = heappop(heap)
        c.append(v)
        if index < n-1:
            heappush(heap, (v - a[index] + a[index + 1],index+1))
    return c


def solve():
    a = arr[0]
    for i in range(1, m):
        a = merge(a, arr[i])
    print(*a)


t = int(input())
for _ in range(t):
    # 数据录入+预处理
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    for i in range(len(arr)):
        arr[i].sort()  # 排序
    solve()
