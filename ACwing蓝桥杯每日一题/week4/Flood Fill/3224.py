"""
https://www.acwing.com/problem/content/3227/
"""
import queue

options = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_fill(lst):
    x, y, char = lst
    x, y = int(x), int(y)
    q = queue.Queue()
    q.put((n - 1 - y, x))
    flag = set()
    while not q.empty():
        xx, yy = q.get()
        draw[xx][yy] = char
        for dx, dy in options:
            x, y = xx + dx, yy + dy
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if draw[x][y] != "-" and draw[x][y] != "+" and draw[x][y] != "|" and (x, y) not in flag:
                flag.add((x, y))
                q.put((x, y))


def draw_line(lst):
    x1, y1, x2, y2 = map(int, lst)
    # 分类讨论得了，懒得动大脑了
    if x1 == x2:
        char = "|"
        y1, y2 = n - 1 - min(y1, y2), n - 1 - max(y1, y2),
        for y in range(y2, y1 + 1):
            if draw[y][x1] == "-" or draw[y][x1] == "+":
                draw[y][x1] = "+"
            else:
                draw[y][x1] = char
    if y1 == y2:
        char = "-"
        x1, x2 = min(x1, x2), max(x1, x2)
        y = n - 1 - y1
        for x in range(x1, x2 + 1):
            if draw[y][x] == "|" or draw[y][x] == "+":
                draw[y][x] = "+"
            else:
                draw[y][x] = char


m, n, q = map(int, input().split(" "))
operate = [list(input().split(" ")) for _ in range(q)]
draw = [["."] * m for _ in range(n)]
for op in operate:
    if op[0] == "1":
        flood_fill(op[1:])
    else:
        draw_line(op[1:])
for i in range(n):
    print("".join(draw[i]))
