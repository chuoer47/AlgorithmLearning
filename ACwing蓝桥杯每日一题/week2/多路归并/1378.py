"""
https://www.acwing.com/problem/content/description/1380/
"""

from math import inf

k, n = map(int, input().split())
arr = list(map(int, input().split()))
count = [0] * k
res = [1]
for _ in range(n):
    ans = inf
    j = -1
    for pivot, value in enumerate(arr):
        tem = res[count[pivot]] * value
        if tem < ans:
            ans = tem
    for pivot, value in enumerate(arr):
        tem = res[count[pivot]] * value
        if tem == ans:
            count[pivot] += 1
    res.append(ans)
print(res[-1])
