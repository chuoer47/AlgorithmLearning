"""
暴力解法
只有10%
"""

n, k = map(int, input().strip().split(" "))
a = list(map(int, input().strip().split(" ")))
ans = []
for i in range(n):
    if i + k - 1 >= n:
        break
    window = a[i:i + k]
    window.sort()
    if k % 2 == 0:
        mid = (window[k // 2] + window[k // 2]) / 2
        if mid != int(mid):
            mid = round(mid, 1)
        else:
            mid = int(mid)
    else:
        mid = window[k // 2]
    ans.append(mid)
for i in ans:
    print(i, end=' ')
