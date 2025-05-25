from math import comb
from typing import List
# 预处理阶乘以及其逆元
max_n = int(1e5+100)
fac = [1] * (max_n + 1)
facinv = [1] * (max_n + 1)

MAX_NUM = int(1e9 + 7)
for i in range(1, max_n + 1):
    fac[i] = fac[i - 1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i], MAX_NUM - 2, MAX_NUM)


def myComb(n, m):
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n - m] % MAX_NUM

class LcaBinaryLifting:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n + 1)]
        for x, y in edges:  # 节点编号从 0 开始
            x -= 1
            y -= 1
            g[x].append((y, 1))
            g[y].append((x, 1))

        depth = [0] * n
        dis = [0] * n
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y, w in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dis[y] = dis[x] + w
                    dfs(y, x)

        dfs(0, -1)

        self.depth = depth



class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        lca = LcaBinaryLifting(edges)
        d = lca.depth
        mx = max(d)

        path_size = mx
        ans = 0
        # 边权为奇数的话
        for i in range(path_size + 1):
            # i个1，path_size-i个2
            if (i + 2 * (path_size - i)) & 1:
                ans += myComb(path_size, i)
                ans %= mod
        return ans
