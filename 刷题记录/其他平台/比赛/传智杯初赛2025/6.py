import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

def solve():
    n,m = map(int,input().split(" "))
    mat = [list(map(int, input().split())) for _ in range(n)]

    # 每个变量 i 有两个字面量：
    #   node = 2*i     表示 flip[i] == 0 (不翻)
    #   node = 2*i + 1 表示 flip[i] == 1 (翻)
    V = 2 * n
    g = [[] for _ in range(V)]
    rg = [[] for _ in range(V)]
    edge_set = set()  # 用于去重边 (u,v)

    def add_imp(u, v):
        # 添加一条有向边 u -> v（并在反图中添加）
        if u == v:  # 无意义的自环可以忽略
            return
        if (u, v) in edge_set:
            return
        edge_set.add((u, v))
        g[u].append(v)
        rg[v].append(u)

    # 对每一列 j，构造 value -> list of (row, state)
    # state: 0 表示使用原列 mat[row][j]
    #        1 表示使用翻转后该列 mat[row][m-j-1]
    for j in range(m):
        d = defaultdict(list)
        # 收集该列所有行两种状态的值
        for i in range(n):
            val0 = mat[i][j]
            val1 = mat[i][m - j - 1]
            d[val0].append((i, 0))
            # 注意：如果 val0 == val1，会在同一 value 下出现两个条目 (i,0) 和 (i,1)
            d[val1].append((i, 1))

        # 对每个相同 value 的组，组内任意两个不同的行、状态组合不能同时成立
        for lst in d.values():
            k = len(lst)
            if k <= 1:
                continue
            # 若组太大，可能产生 k^2 较多边；但这是问题本身的约束数
            # 我们跳过相同行的配对（同一行两个状态之间不存在约束）
            for a in range(k):
                i, s = lst[a]
                u = 2 * i + s
                for b in range(a + 1, k):
                    ii, t = lst[b]
                    if i == ii:
                        continue
                    v = 2 * ii + t
                    # 约束: 不能同时 (u 被选中) AND (v 被选中)
                    # 转为 2-SAT: (not u) or (not v)
                    # 即 u -> not v , v -> not u
                    add_imp(u, 2 * ii + (1 - t))
                    add_imp(v, 2 * i + (1 - s))

    # Kosaraju 求 SCC
    visited = [False] * V
    order = []

    def dfs(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs(w)
        order.append(u)

    for u in range(V):
        if not visited[u]:
            dfs(u)

    comp = [-1] * V
    cid = 0

    def rdfs(u, c):
        comp[u] = c
        for w in rg[u]:
            if comp[w] == -1:
                rdfs(w, c)

    for u in reversed(order):
        if comp[u] == -1:
            rdfs(u, cid)
            cid += 1

    # 检查矛盾
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("No")
            return

    # 构建一个合法解：通常取 comp[lit_false] < comp[lit_true] 为 True/False 判定
    # （Kosaraju 中 comp 值的大小序可用于决定）
    ans = [0] * n
    for i in range(n):
        # 若 comp[false] < comp[true] ，则选 true (翻转)
        # 这是常见的排序约定（若你怀疑，可小样例验证）
        if comp[2 * i] < comp[2 * i + 1]:
            ans[i] = 1
        else:
            ans[i] = 0

    print("Yes")
    k = sum(ans)
    print(k)
    if k > 0:
        print(*[i + 1 for i in range(n) if ans[i] == 1])


if __name__ == "__main__":
    solve()
