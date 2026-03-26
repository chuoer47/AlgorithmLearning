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
    for id in tt:
        if tt[id] >= k:
            res.add(id)


n, d, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(0, n)]
arr.sort()
# print(arr)
res = set()
cnt = Counter()
left, right = 0, 0  # left指向最开始的时间的下标，right指向最开始（第一个）的不满足的下标
for right in range(0, n):
    if arr[right][0] - arr[left][0] >= d:
        while arr[right][0] - arr[left][0] >= d:
            cnt[arr[left][1]] -= 1
            left += 1
    cnt[arr[right][1]] += 1
    if cnt[arr[right][1]] == k:
        res.add(arr[right][1])

    # print(cnt)
res = list(res)
res.sort()
# print("res=" + str(res))
for i in res:
    print(i)
