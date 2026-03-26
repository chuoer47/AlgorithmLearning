"""
https://www.acwing.com/problem/content/1240/
该写法会导致超时，需要把check方法融合
"""

from collections import Counter


def check(left, right):
    tem = []
    for i in range(left, right):
        ts, id = arr[i]
        tem.append(id)
    tt = dict(Counter(tem))
    # print("tem:")
    # print(tem)
    # print(tt)
    for id in tt:
        if tt[id] >= k:
            res.add(id)


n, d, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(0, n)]
arr.sort()
res = set()
left, right = 0, 0  # left指向最开始的时间的下标，right指向最开始（第一个）的不满足的下标
for left in range(0, n):
    if left != 0 and arr[left][0] == arr[left - 1][0]:  # 前一个时间和后一个时间一样，则跳过
        continue
    right = left
    while right < n and arr[right][0] < arr[left][0] + d:
        right += 1
    check(left, right)
res = list(res)
res.sort()
for i in res:
    print(i)
