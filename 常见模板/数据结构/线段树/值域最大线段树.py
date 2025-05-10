class SegmentTree:
    # 基于值域的线段树
    def __init__(self, u):
        self.u = u
        self.tr = [0] * (4 * u)

    def modify(self, pos, val):
        self._modify(1, 1, self.u, val, pos)

    def _modify(self, o, l, r, val, pos):
        if l == r:
            self.tr[o] = val
            return
        mid = (l + r) >> 1
        if pos <= mid:
            self._modify(o << 1, l, mid, val, pos)
        else:
            self._modify((o << 1) + 1, mid + 1, r, val, pos)
        self.tr[o] = max(self.tr[o << 1], self.tr[(o << 1) + 1])

    def query(self, L, R):
        return self._query(1, 1, self.u, L, R)

    def _query(self, o, l, r, L, R):
        if L <= l and r <= R:
            return self.tr[o]
        ans = 0
        mid = (l + r) >> 1
        if mid >= L:
            ans = self._query(o << 1, l, mid, L, R)
        if mid < R:
            ans = max(ans, self._query((o << 1) + 1, mid + 1, r, L, R))
        return ans