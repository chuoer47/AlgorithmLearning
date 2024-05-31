"""
https://www.acwing.com/problem/content/181/
"""
import queue

OK = "#12345678x"


def lst2str(lst):
    res = ""
    for i in lst:
        res += i
    return "#" + res


def chess2str(chess):
    lst = chess[1][1:4] + chess[2][1:4] + chess[3][1:4]
    return lst2str(lst)


def check(s):
    return s == OK


name = ["l", "r", "u", "d"]
options = [(0, -1), (0, 1), (-1, 0), (1, 0)]
s = input().split(" ")
# 下面判断是否无解：
solve = s.copy()
solve.remove("x")
# 计算逆序对
ni = 0
for i in range(8):
    for j in range(i + 1, 8):
        if solve[i] > solve[j]:
            ni += 1
# 逆序对为奇数则无解
if ni % 2 == 1:
    print("unsolvable")
    exit(0)  # TODO：这里简单写了，提交到算法网站要改一下，不然会报错
s = lst2str(s)
state = set()  # 记录状态
state.add(s)
stack = queue.Queue()  # 使用队列
stack.put((s, ""))
res = ""
# BFS
while stack:
    # print(stack)
    s, op = stack.get()
    if check(s):
        res = op
        break
    chess = [[0] * 5 for _ in range(5)]
    # 棋盘初始化
    chess[1][1:4] = s[1:4]
    chess[2][1:4] = s[4:7]
    chess[3][1:4] = s[7:]
    for i in range(1, 4):
        for j in range(1, 4):
            if chess[i][j] == "x":
                x, y = i, j
    for pivot, option in enumerate(options):
        l, r = option
        xx, yy = x + l, y + r
        if chess[xx][yy] == 0:  # 没法交换
            continue
        else:  # 交换
            chess[x][y], chess[xx][yy] = chess[xx][yy], chess[x][y]
            ss = chess2str(chess)
            if ss not in state:  # 检查是否存在该状态
                state.add(ss)
                stack.put((ss, op + name[pivot]))
            chess[x][y], chess[xx][yy] = chess[xx][yy], chess[x][y]
print(res)
