"""
https://www.acwing.com/problem/content/4410/
"""


def find(): # 找到同一地点的多枚炸弹
    res = 0
    for i in has_mine:
        for j in mine:
            if j == i:
                res += 1
    return res


def dfs(x, y, r):
    for i in mine:
        if i not in has_mine:
            xx, yy, rr = i
            if (xx - x) ** 2 + (yy - y) ** 2 <= r ** 2:
                has_mine.append([xx, yy, rr])
                # 递归炸弹
                dfs(xx, yy, rr)


n, m = map(int, input().split(" "))
mine = [list(map(int, input().split(" "))) for _ in range(n)]
mineFire = [list(map(int, input().split(" "))) for _ in range(m)]
has_mine = []
# print(mine, has_mine)
for i in mineFire:
    # 开炸
    x, y, r = i
    dfs(x, y, r)
res = find()
print(res)
