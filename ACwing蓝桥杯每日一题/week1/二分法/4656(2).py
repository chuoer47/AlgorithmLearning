"""
原题链接：
https://www.acwing.com/problem/content/4659/
该解法使用了堆，优化了一下每次插入堆前的操作，但是还是超时了
"""

import heapq

n, m = map(int, input().split(" "))
arr = []
for i in range(0, n):
    a, b = map(int, input().split(" "))
    a, b = -a, -b
    arr.append((a, b))
heapq.heapify(arr)
res = 0
while m != 0:
    # 优化算法，一次取俩个数进行比较
    a, b = heapq.heappop(arr)
    # 当都升级完毕后，不再操作
    if a == 0:
        break
    a1, b1 = heapq.heappop(arr)
    a, b = -a, -b
    a1, b1 = -a1, -b1
    da = a - a1
    dd = da // b + 1  # 间隔
    if m >= dd:
        m -= dd
        res += (2 * a - (dd-1) * b) * dd // 2
        a = max(a - dd * b,0)
    else:
        res += (2 * a - (m-1) * b) * m // 2
        break
    if m == 0:
        break
    heapq.heappush(arr, (-a1, -b1))
    heapq.heappush(arr, (-a, -b))
print(res)
