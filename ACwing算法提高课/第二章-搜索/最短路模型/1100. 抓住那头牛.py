"""
https://www.acwing.com/problem/content/1102/
"""
from collections import deque

# 预处理数据
n, k = map(int, input().split(" "))
flag = set()
dis = dict()
choice = [
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: 2 * x
]

# 洪水漫灌策略
stack = deque()
stack.append((n, 0))

# 找到最短路的路径大小
while stack:
    x, step = stack.popleft()
    if x in flag:
        continue
    flag.add(x)
    if x in dis.keys():
        dis[x] = min(dis[x], step)
    else:
        dis[x] = step
    if x > k:  # 剪枝，不然很结果会跑到天昏地暗
        stack.append((x - 1, step + 1))
    else:
        # 遍历当前点的可选
        for f in choice:
            if f(x) not in flag and f(x) >= 0:
                stack.append((f(x), step + 1))

print(dis[k])
