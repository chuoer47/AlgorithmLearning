"""
原题链接：
https://www.acwing.com/problem/content/4659/
该解法使用了堆，贪心算法，但是会超时
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
    a, b = heapq.heappop(arr)
    a, b = -a, -b
    # 当都升级完毕后，不再操作
    if a == 0:
        break
    res += a
    heapq.heappush(arr, (-max(0, a - b), -b))
    m -= 1
print(res)
