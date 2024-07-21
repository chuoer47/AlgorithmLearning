"""
https://www.acwing.com/problem/content/1099/
"""

n, m = map(int, input().split(" "))
area = [input().strip() for _ in range(n)]
flag = [[0] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == "W" and not flag[i][j]:
            ans += 1
            stack = [(i, j)]
            # 使用栈代替广搜，思路更加清晰
            while stack:
                x, y = stack.pop()
                flag[x][y] = 1
                # 遍历八个点
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if area[x + dx][y + dy] == "W" and not flag[x + dx][y + dy]:
                                stack.append((x + dx, y + dy))
print(ans)
