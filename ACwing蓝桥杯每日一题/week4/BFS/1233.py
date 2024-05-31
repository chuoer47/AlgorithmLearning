"""
https://www.acwing.com/problem/content/1235/
"""
options = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    global flag
    while st:
        x, y = st.pop()  # 获取坐标
        ff = False  # 表示是否被淹没
        for option in options:
            l, r = option
            xx, yy = x + l, y + r  # 新的坐标
            if (xx,yy) in verify:  # 存在岛屿
                if (xx, yy) in island_set:
                    island_set.remove((xx, yy))
                    st.append((xx, yy))
            else:
                ff = True  # 被淹没了
        if not ff:
            flag = True  # 存在该岛屿


n = int(input())
island_set = set()  # 使用set来存储岛屿坐标
verify = set()
for i in range(n):
    t = list(input())
    for j in range(n):
        if t[j] == "#":
            verify.add((i,j))
            island_set.add((i, j))  # 将岛屿坐标添加到set中
res = 0

while island_set:  # 使用set的布尔值来判断是否为空
    # print(island_set)
    flag = False
    st = [island_set.pop()]  # 从set中弹出一个元素
    bfs()
    if not flag:  # 完全被淹没
        res += 1
print(res)