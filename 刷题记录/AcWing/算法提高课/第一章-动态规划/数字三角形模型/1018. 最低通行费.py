"""
https://www.acwing.com/problem/content/description/1020/
难度居然在数据录入...
"""

n = int(input())
weight = [[int(i) for i in input().strip().split(" ") if i] for _ in range(n)]

for i in range(1,n):
    weight[0][i] += weight[0][i-1]
    weight[i][0] += weight[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        weight[i][j] = min(weight[i - 1][j], weight[i][j - 1]) + weight[i][j]
print(weight[-1][-1])
