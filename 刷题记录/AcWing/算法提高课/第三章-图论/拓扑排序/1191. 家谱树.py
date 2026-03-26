"""
https://www.acwing.com/problem/content/1193/

拓扑排序模板题
第一次打，感觉不难，主要是先看了视频hhh
"""


def topsort():
    """拓扑排序"""
    from collections import deque
    q = deque()
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        ans.append(now)  # 录入
        for fa in graph[now]:
            in_deg[fa] -= 1
            if in_deg[fa] == 0:
                q.append(fa)


if __name__ == '__main__':
    n = int(input())
    # 建图
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []
    in_deg = [0] * (n + 1)
    # 录入数据
    for i in range(1, n + 1):
        sons = list(map(int, input().strip().split(" ")))
        for s in sons[:-1]:
            graph[s].append(i)
            in_deg[i] += 1
    # 拓扑排序
    ans = []
    topsort()
    ans.reverse()  # 逆转一下
    print(*ans)
