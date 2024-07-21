"""
https://www.acwing.com/problem/content/1078/
"""
from collections import deque

# 预处理数据
n = int(input())
area = [list(map(int, input().strip().split(" "))) for _ in range(n)]  # 迷宫
flag = [[0] * n for _ in range(n)]
dis = [[n * n] * n for _ in range(n)]
stack = deque()
stack.append((0, 0, 0))
choice = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]

# 先找到最短路的路径大小
while stack:
    x, y, step = stack.popleft()
    if flag[x][y]:
        continue
    flag[x][y] = 1
    dis[x][y] = min(dis[x][y], step)
    # 上下左右遍历当前点的可选方向
    for dx, dy in choice:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if not flag[x + dx][y + dy] and area[x + dx][y + dy] == 0:
                stack.append((x + dx, y + dy, step + 1))

# 在倒推路径是什么
length = dis[-1][-1]
path = []
x, y = n - 1, n - 1
while length:
    for dx, dy in choice:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if dis[x + dx][y + dy] == length:
                path.append([x + dx, y + dy])
                x, y = x + dx, y + dy
                length -= 1
                break
path.append([0,0])

# 输出
path.reverse()
for i in path:
    print(*i)

