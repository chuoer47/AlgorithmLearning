"""
https://www.acwing.com/problem/content/description/3468/
python深搜会出现segment错误
"""
import sys

sys.setrecursionlimit(10000000)


def dfs(index):
    if not nxt[index]:
        return 1  # 根节点
    maxD = -1
    for i in nxt[index]:
        d = dfs(i)
        if d > maxD:
            res[index] = i
            maxD = d
    return maxD + 1


# 录入数据
n = int(input())
lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
father = [-1] * n
# 处理边
nxt = [[] for _ in range(n)]
for i in range(n):
    if lst[i][0] != 0:
        for j in lst[i][1:]:
            nxt[i].append(j)
            father[j] = i
        nxt[i].sort()
# 深搜
res = [-1] * n
root = -1  # 找到根结点
for i in range(n):
    if father[i] == -1:
        root = i
        break
# 利用栈深搜
length = dfs(root)
i = root
ans = [root]
while res[i] != -1:
    ans.append(res[i])
    i = res[i]
print(length)
print(*ans)
