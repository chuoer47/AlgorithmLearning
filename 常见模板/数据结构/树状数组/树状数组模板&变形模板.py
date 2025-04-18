class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class FenwickTree:
    # 树状数组实现 区间修改 + 区间求和的功能
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)  # 维护的是d[i]；即nums[i]的差分数组
        self.itree = [0] * (n + 1)  # 维护的是b[i]=i*d[i];即一个新定义的差分数组

    def update(self, i: int, val: int) -> None:
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def iupdate(self, i, val):
        while i <= self.n:
            self.itree[i] += val
            i += i & -i

    def add(self, x, val):
        # 实现单边区间加
        self.update(x, val)
        self.iupdate(x, x * val)

    def rangeAdd(self, l, r, val):
        # 实现区间修改
        self.add(l, val)
        self.add(r + 1, -val)

    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    def iper(self, i):
        res = 0
        while i > 0:
            res += self.itree[i]
            i &= i - 1
        return res

    def rangeX(self, x):
        # 区间单边查询
        a = self.pre(x)
        b = self.iper(x)
        return (x + 1) * a - b

    def rangeQuery(self, l, r):
        return self.rangeX(r) - self.rangeX(l - 1)


from cmath import inf


class BinaryIndexedMaxTree:
    # 权值树状数组
    __slots__ = ["n", "c"]

    def __init__(self, n):

        self.n = n
        self.c = [-inf] * (n + 1)

    def update(self, x: int, delta: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], delta)
            x += x & -x

    def query(self, x: int):
        s = -inf
        while x > 0:
            s = max(s, self.c[x])
            x -= x & -x
        return s
