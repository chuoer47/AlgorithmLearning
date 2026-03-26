"""
https://www.acwing.com/problem/content/1209/
这道题目可以直接使用求树的直径，但是题目特殊性保证了直径一定会经过首都，因此可以只用一次DFS
"""
import sys

sys.setrecursionlimit(1000000)


def dfs(p, father):
    if not dis[p]:  # 没有路了
        return 0
    one, two = 0, 0
    for np, value in dis[p]:
        tem = 0
        if np != father:
            tem = dfs(np, p) + value
        if tem > one:
            one, two = tem, one
        elif tem > two:
            two = tem
        global ans
        ans = max(ans, one + two)
    return one


n = int(input())
dis = [[] for _ in range(n + 10)]
for _ in range(n - 1):
    p, q, d = map(int, input().split(" "))
    dis[p].append((q, d))
    dis[q].append((p, d))
ans = 0
dfs(1, -1)
# print(dis)
ans = ans*10 + ans*(1+ans)//2
print(ans)
