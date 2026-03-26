"""
https://www.acwing.com/problem/content/1100/
"""


def check(x, y, dx, dy):
    "用来检查两个房间是否连通"
    tem = [8, 4, 2, 1]
    value = area[x][y]
    has = set()
    for t in tem:
        if value >= t:
            value -= t
            has.add(t)
    go = 0
    if dx == 1 and dy == 0:
        go = 8
    elif dx == -1 and dy == 0:
        go = 2
    elif dx == 0 and dy == 1:
        go = 4
    else:
        go = 1
    return go not in has


n, m = map(int, input().strip().split(" "))
area = [list(map(int, input().strip().split(" "))) for _ in range(n)]
flag = [[0] * m for _ in range(n)]
choice = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0  # 记录房间个数
maxArea = 0  # 记录房间最大面积
for i in range(n):
    for j in range(m):
        if not flag[i][j]:
            ans += 1  # 房间数加一
            nowArea = 0
            stack = [(i, j)]
            # 使用栈代替广搜，思路更加清晰
            while stack:
                x, y = stack.pop()
                if flag[x][y]:
                    continue
                flag[x][y] = 1
                nowArea += 1
                # 遍历四个点
                for dx, dy in choice:
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        if check(x, y, dx, dy) and not flag[x + dx][y + dy]:
                            stack.append((x + dx, y + dy))
            maxArea = max(maxArea, nowArea)

# 输出
print(ans)
print(maxArea)
