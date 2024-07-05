from collections import deque


class Edge:
    def __init__(self, v=0, w=0):
        self.v = v
        self.w = w

maxn = 999
e = [[Edge() for i in range(maxn)] for j in range(maxn)]
dis = [0x3F3F3F3F] * maxn
cnt = [0] * maxn
vis = [False] * maxn

q = deque()


def spfa(n, s):
    dis[s] = 0
    vis[s] = True
    q.append(s)
    while q:
        u = q.popleft()
        vis[u] = False
        for ed in e[u]:
            v, w = ed.v, ed.w
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                cnt[v] = cnt[u] + 1  # 记录最短路经过的边数
                if cnt[v] >= n:
                    return False
                # 在不经过负环的情况下，最短路至多经过 n - 1 条边
                # 因此如果经过了多于 n 条边，一定说明经过了负环
                if not vis[v]:
                    q.append(v)
                    vis[v] = True