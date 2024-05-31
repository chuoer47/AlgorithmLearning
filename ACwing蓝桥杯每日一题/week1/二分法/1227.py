"""
https://www.acwing.com/problem/content/1229/
"""


def cal(lst: list, case: int):
    a, b = min(lst), max(lst),
    if case > a:
        return 0
    return (a // case) * (b // case)


def judge(case):
    sum = 0
    for i in arr:
        sum += cal(i, case)
    return sum >= k


n, k = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for i in range(0, n)]
# 利用二分法找到最大的FALSE 或 找到最小的TURE
l, r = 1, 100010
while l < r:
    mid = (l + r) // 2
    if not judge(mid):
        r = mid
    else:
        l = mid + 1
print(r-1)
