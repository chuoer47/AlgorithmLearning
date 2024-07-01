"""
https://www.acwing.com/problem/content/127/
"""

n = int(input())
lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
lst.sort(key=lambda x: sum(x))
sumLst = [0]
for i in range(1, n):
    sumLst.append(sumLst[i - 1] + lst[i-1][0])
res = float('-inf')
for i in range(0, n):
    res = max(res, sumLst[i] - lst[i][1])
print(res)
