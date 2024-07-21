"""
https://www.acwing.com/problem/content/1108/
"""

n = int(input())
area = [list(map(int, input().strip().split(" "))) for _ in range(n)]
flag = [[0] * n for _ in range(n)]
peak, bottom = 0, 0  # 山峰和山谷
for i in range(n):
    for j in range(n):
        if not flag[i][j]:
            now = area[i][j]
            isPeak, isBottom = 0, 0
            stack = [(i, j)]
            # 使用栈代替广搜，思路更加清晰
            while stack:
                x, y = stack.pop()
                if flag[x][y]:
                    continue
                flag[x][y] = 1
                # 遍历八个点
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= x + dx < n and 0 <= y + dy < n:
                            tem = area[x + dx][y + dy]
                            if area[x + dx][y + dy] == now and not flag[x + dx][y + dy]:
                                stack.append((x + dx, y + dy))
                            elif area[x + dx][y + dy] > now:
                                isBottom = 1
                            elif area[x + dx][y + dy] < now:
                                isPeak = 1
            if isPeak == 1 and isBottom == 0:  # 是山峰
                peak += 1
            elif isPeak == 0 and isBottom == 1:
                bottom += 1

if peak == 0 and bottom == 0:
    print(1, 1)
else:
    print(peak, bottom)
