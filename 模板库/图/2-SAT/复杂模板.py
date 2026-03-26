import sys
sys.setrecursionlimit(1 << 25)

class TwoSAT:
    def __init__(self, n):
        """
        n: 变量个数 (编号 0..n-1)
        节点编号约定（常用竞赛约定）：
            literal True  for variable i  -> node = 2*i
            literal False for variable i  -> node = 2*i ^ 1  (即 2*i+1)
        图节点总数 = 2 * n
        """
        self.n = n
        self.N = 2 * n
        self.g = [[] for _ in range(self.N)]      # implication graph
        self._assignment = None

    # ---------- 基本工具 ----------
    def lit(self, var, is_true=True):
        """把 (var, is_true) 映射到节点 id"""
        return (2 * var) ^ (0 if is_true else 1)

    def neg(self, x):
        """取反字面量节点 id"""
        return x ^ 1

    def add_implication(self, u, v):
        """添加蕴含边 u -> v（u, v 为字面量节点 id）"""
        self.g[u].append(v)

    # (a OR b) 等价于 (¬a -> b) 且 (¬b -> a)
    def add_or(self, a, b):
        self.add_implication(self.neg(a), b)
        self.add_implication(self.neg(b), a)

    def add_clause(self, var1, val1, var2, val2):
        """高层接口：添加 (var1 is val1) OR (var2 is val2)"""
        a = self.lit(var1, val1)
        b = self.lit(var2, val2)
        self.add_or(a, b)

    def add_xor(self, var1, var2):
        """x ⊕ y"""
        a = self.lit(var1, True)
        b = self.lit(var2, True)
        # (a xor b) <=> (a ∨ b) & (¬a ∨ ¬b) but using add_or on lits/negations
        self.add_or(a, b)
        self.add_or(self.neg(a), self.neg(b))

    def add_equiv(self, var1, var2):
        """x == y"""
        a = self.lit(var1, True)
        b = self.lit(var2, True)
        self.add_or(self.neg(a), b)
        self.add_or(self.neg(b), a)
        self.add_or(a, self.neg(b))
        self.add_or(b, self.neg(a))

    def add_true(self, var):
        """强制 var = True"""
        x = self.lit(var, True)
        self.add_implication(self.neg(x), x)

    def add_false(self, var):
        """强制 var = False"""
        x = self.lit(var, True)
        self.add_implication(x, self.neg(x))

    # ---------- Tarjan SCC 判断可满足性 ----------
    def solve(self):
        """
        返回：
            - list of booleans (长度 n) 表示一个可行赋值（True/False）
            - 若无解返回 None
        """
        N = self.N
        g = self.g

        dfn = [0] * N
        low = [0] * N
        instk = [False] * N
        stk = []
        comp = [-1] * N
        time = 1

        def tarjan(u):
            nonlocal time
            dfn[u] = low[u] = time
            time += 1
            stk.append(u)
            instk[u] = True
            for v in g[u]:
                if dfn[v] == 0:
                    tarjan(v)
                    low[u] = low[u] if low[u] < low[v] else low[v]
                elif instk[v]:
                    if low[u] > dfn[v]:
                        low[u] = dfn[v]
            if dfn[u] == low[u]:
                # pop component
                while True:
                    x = stk.pop()
                    instk[x] = False
                    comp[x] = u
                    if x == u:
                        break

        for i in range(N):
            if dfn[i] == 0:
                tarjan(i)

        assignment = [False] * self.n
        for i in range(self.n):
            if comp[2*i] == comp[2*i ^ 1]:
                # xi 与 ¬xi 在同一 SCC -> 无解
                self._assignment = None
                return None
            # 比较两个节点的 SCC 根节点编号（这里用 comp 值）
            # 通常用 Tarjan 时，comp 值的大小并不严格等于拓扑序，
            # 但由于我们以 "root node index" 作为 comp 标识，并且 tarjan
            # 的 root 被分配为遍历时的节点序号，下面判断 assignment 可用。
            assignment[i] = comp[2*i] > comp[2*i ^ 1]

        self._assignment = assignment
        return assignment

    # ---------- 辅助：从整数字面量格式解析 ----------
    @staticmethod
    def lit_from_int(x):
        """
        常见输入格式：整数表示字面量（如 DIMACS/竞赛题）
         - 正数 k 表示 x_k 为 True（变量编号从 1 开始）
         - 负数 -k 表示 x_k 为 False
        返回节点 id (0-based var index internally)
        """
        if x > 0:
            return (2 * (x - 1)) ^ 0
        else:
            return (2 * ((-x) - 1)) ^ 1

    def add_clause_from_ints(self, a, b):
        """把两个整数字面量 a b 转换并加入 (a OR b)"""
        A = TwoSAT.lit_from_int(a)
        B = TwoSAT.lit_from_int(b)
        self.add_or(A, B)


# ----------------- 使用示例 -----------------
if __name__ == "__main__":
    # ---------- 示例 A: 通过 API 构造 ----------
    # 3 个变量 x0, x1, x2
    ts = TwoSAT(3)

    # 添加约束：
    # x0 -> x1  等价 (¬x0 ∨ x1)
    ts.add_clause(0, False, 1, True)   # (x0 is False) OR (x1 is True)

    # x1 XOR x2
    ts.add_xor(1, 2)

    # x0 = True
    ts.add_true(0)

    ans = ts.solve()
    if ans is None:
        print("API 示例：无解")
    else:
        print("API 示例：可行解 ->", ans)   # [True/False...]

    # ---------- 示例 B: 从 stdin 读取常见格式 ----------
    # 格式：
    # 第一行: n m
    # 接下来的 m 行: 两个整数 a b 表示 (a OR b)；正数 k 表示 x_k；负数 -k 表示 ¬x_k
    #
    # 例如：
    # 3 3
    # -1 2    (¬x1 ∨ x2)   即 x1 -> x2
    # 2 -3    (x2 ∨ ¬x3)
    # 1 1     (x1)         单文字句 (x1 ∨ x1)
    #
    # 下面是用字符串模拟输入的例子；实际比赛中把 input_lines 换为 sys.stdin 即可。
    input_lines = """\
3 3
-1 2
2 -3
1 1
"""
    data = iter(input_lines.strip().split())
    n = int(next(data))
    m = int(next(data))
    ts2 = TwoSAT(n)
    for _ in range(m):
        a = int(next(data))
        b = int(next(data))
        ts2.add_clause_from_ints(a, b)

    res = ts2.solve()
    if res is None:
        print("stdin 示例：无解")
    else:
        # 输出为 0/1 序列（或 True/False）
        print("stdin 示例：可行解 ->", res)
        print("stdin 示例：按 0/1 输出 ->", [1 if x else 0 for x in res])
