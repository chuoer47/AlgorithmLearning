"""
https://www.acwing.com/problem/content/1222/
"""
import sys
sys.setrecursionlimit(100000)

def dfs(pivot, father):
    w = weight[pivot]
    for s in graph[pivot]:
        if s == father:
            continue
        dfs(s, pivot)
        w += max(0, f[s])
    f[pivot] = w


n = int(input())
weight = [-1] + list(map(int, input().split(" ")))  # 方便下标操作
graph = [[] for _ in range(n + 10)]
for _ in range(n - 1):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)
res = -float('inf')
f = [-1] * (n + 10)
dfs(1, -1)
print(max(f))
