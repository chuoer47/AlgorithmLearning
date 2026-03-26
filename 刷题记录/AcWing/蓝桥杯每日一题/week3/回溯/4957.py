"""
https://www.acwing.com/problem/content/description/4960/
"""


def dfs(now, last):  # now表示已经降落的飞机个数，last表示最近的一个飞机降落的时间
    global flag
    if now >= n:
        flag = True
        return
    if flag:
        return
    for i in range(n):
        if not use[i]:
            if lst[i][1] < last:
                return
            use[i] = 1
            if lst[i][0] >= last:
                dfs(now + 1, lst[i][0] + lst[i][2])
            else:
                dfs(now + 1, last + lst[i][2])
            use[i] = 0


use = [0] * 20  # 表示使用数组
res = []
t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split(" "))) for _ in range(n)]
    for i in range(n):  # 最晚的降落时间
        lst[i][1] += lst[i][0]
    flag = False
    dfs(0, 0)
    if flag:
        res.append("YES")
    else:
        res.append("NO")

# 输出结果
for i in range(t):
    print(res[i])
