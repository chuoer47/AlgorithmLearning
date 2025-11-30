class TwoSAT:
    def __init__(self, n):
        """
        n: 变量数量，变量编号为 0..n-1
        每个变量 xi 有两个节点：
            xi     -> 2*i
            ¬xi    -> 2*i^1  (即 2*i+1)
        图大小为 2*n
        """
        self.n = n
        self.N = 2 * n
        self.g = [[] for _ in range(self.N)]

    # === 工具：取反 ===
    def neg(self, x):
        return x ^ 1

    # === 添加子句: (x OR y) ===
    # (x ∨ y) 等价于 (¬x → y) 且 (¬y → x)
    # x, y 都必须以 "节点编号" 形式给，即:
    #   xi     = 2*i
    #   ¬xi    = 2*i + 1 = 2*i^1
    def add_or(self, x, y):
        self.g[self.neg(x)].append(y)
        self.g[self.neg(y)].append(x)

    # === 添加 xi = True ===
    # 即 (xi) 可视为 (¬xi → xi)
    def add_true(self, x):
        self.g[self.neg(x)].append(x)

    # === 添加 xi = False ===
    # 即 (¬xi) 可视为 (xi → ¬xi)
    def add_false(self, x):
        self.g[x].append(self.neg(x))

    # === 添加 x = y ===
    def add_equiv(self, x, y):
        self.add_or(x, self.neg(y))
        self.add_or(self.neg(x), y)

    # === 添加 x != y ===
    def add_xor(self, x, y):
        self.add_or(x, y)
        self.add_or(self.neg(x), self.neg(y))

    # === Tarjan 求 SCC 判断可解性 ===
    def solve(self):
        N = self.N
        g = self.g

        dfn = [0] * N
        low = [0] * N
        instk = [False] * N
        stk = []
        now = 1
        comp = [-1] * N   # 每个节点所属的强连通分量（SCC）

        def tarjan(u):
            nonlocal now
            dfn[u] = low[u] = now
            now += 1
            stk.append(u)
            instk[u] = True

            for v in g[u]:
                if dfn[v] == 0:
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                elif instk[v]:
                    low[u] = min(low[u], dfn[v])

            # root of SCC
            if dfn[u] == low[u]:
                while True:
                    x = stk.pop()
                    instk[x] = False
                    comp[x] = u
                    if x == u:
                        break

        # run tarjan
        for i in range(N):
            if dfn[i] == 0:
                tarjan(i)

        # 检查冲突：若 xi 与 ¬xi 在同一个 SCC，则无解
        assignment = [False] * self.n
        for i in range(self.n):
            if comp[2*i] == comp[2*i^1]:
                return None  # 无解
            # 逆拓扑序：SCC 编号大者为 False/True，这里用 comp 值替代
            assignment[i] = comp[2*i] > comp[2*i^1]

        return assignment
if __name__ == '__main__':
    """
    题目：
    给定 3 个变量 x0, x1, x2
    请满足以下条件：
    x0 → x1
    x1 XOR x2
    x0 = True
    变量 i：
    xi  = 2*i
    ¬xi = 2*i^1 = 2*i + 1
    """
    # 建立 2-SAT，变量数量=3
    ts = TwoSAT(3)

    # x0 -> x1 等价于 (¬x0 OR x1)
    ts.add_or(ts.neg(2 * 0), 2 * 1)

    # x1 XOR x2
    ts.add_xor(2 * 1, 2 * 2)

    # x0 = True
    ts.add_true(2 * 0)

    ans = ts.solve()

    if ans is None:
        print("无解")
    else:
        print("可行解：", ans)
