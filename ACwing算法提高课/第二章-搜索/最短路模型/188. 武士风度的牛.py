"""
https://www.acwing.com/problem/content/190/
"""
from collections import deque

# 预处理
c, r = map(int, input().split(" "))
area = [input().strip() for _ in range(r)]
for i in range(r):
    for j in range(c):
        if area[i][j] == "K":
            begin = [i, j]
        if area[i][j] == "H":
            end = [i, j]

choice = [[1, 2], [-1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]

flag = [[0] * c for _ in range(r)]
dis = [[r * c] * c for _ in range(r)]
stack = deque()
stack.append((begin[0], begin[1], 0))

# 先找到最短路的路径大小
while stack:
    x, y, step = stack.popleft()
    if flag[x][y]:
        continue
    flag[x][y] = 1
    dis[x][y] = min(dis[x][y], step)
    if x == end[0] and y == end[1]:
        break
    # 上下左右遍历当前点的可选方向
    for dx, dy in choice:
        if 0 <= x + dx < r and 0 <= y + dy < c:
            if not flag[x + dx][y + dy] and area[x + dx][y + dy] !="*":
                stack.append((x + dx, y + dy, step + 1))

print(dis[end[0]][end[1]])
