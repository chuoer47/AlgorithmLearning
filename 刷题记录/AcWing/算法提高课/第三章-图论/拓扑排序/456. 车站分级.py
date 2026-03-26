"""
https://www.acwing.com/problem/content/description/458/
"""


def topsort():
    """拓扑排序"""
    global ans
    from collections import deque
    q = deque()
    for i in range(1, n + m + 1):
        if in_deg[i] == 0:
            q.append((i, 1))
    while q:
        now, rank = q.popleft()
        ans = max(ans, rank)  # 记录当前最大等级
        for fa in graph[now]:
            in_deg[fa] -= 1
            if in_deg[fa] == 0:
                # 这里判断是否为虚拟源点，是的话就不加1
                # 其实普遍的方法是使用带权边
                # 这里偷懒了
                if now <= n:
                    q.append((fa, rank + 1))
                else:
                    q.append((fa, rank))


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    # 建图，这里要使用虚拟源点，减少建立边的次数
    graph = dict()
    for i in range(1, n + m + 1):
        graph[i] = set()
    in_deg = [0] * (n + m + 1)
    # 录入数据
    for vi in range(n + 1, m + n + 1):  # vi表示虚拟点
        dataRow = list(map(int, input().strip().split(" "))) # 一行数据
        num, station = dataRow[0], dataRow[1:]
        # 使用集合方便操作
        all = set(range(station[0], station[-1] + 1))
        small = all.difference(station)
        station = set(station)
        # 添加边
        graph[vi] |= station  # 集合并操作
        for s in small:
            graph[s].add(vi)
    # 计算入度，由于采用了虚拟源点，只能这样子计算，不过复杂度不算高
    for i in range(1, n + m + 1):
        for j in range(1, n + m + 1):
            if i in graph[j]:
                in_deg[i] += 1
    # 拓扑排序
    ans = 1
    topsort()
    print(ans)
