"""
https://www.acwing.com/problem/content/5399/
"""
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, m)]
darr = [0 for _ in range(0, n ** 2 + 10)]
for i in range(len(arr)):
    x1, y1, x2, y2 = arr[i]
    for j in range(x1, x2 + 1):
        start = n * (j - 1) + y1
        end = n * (j - 1) + y2 + 1
        darr[start] += 1
        darr[end] -= 1
res = [0 for _ in range(0, n ** 2 + 10)]
for i in range(1, len(res)):
    res[i] = (res[i - 1] + darr[i]) % 2
for i in range(0, n):
    tem = res[1 + i * n:1 + i * n + n]
    tt = ""
    for j in range(len(tem)):
        tt += str(tem[j])
    print(tt)

