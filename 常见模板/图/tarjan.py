from typing import List


class TARJAN:
    def __init__(self, n: int, g: List[List[int]]):
        # 记录结点的当前时间戳和最早时间戳,从根开始的一条路径上dfn 严格递增，low 严格非降
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.bridge = []  # 桥
        self.flag = [False] * n  # 是否是割点
        self.g = g

    def tarjan(self, o: int, f: int, t: int) -> None:
        self.dfn[o] = t
        self.low[o] = t
        c = 0
        for child in self.g[o]:
            if child != f:
                if self.dfn[child] == -1:
                    c += 1
                    self.tarjan(child, o, t + 1)
                    self.low[o] = min(self.low[o], self.low[child])
                    # 找到割点, 非root,有儿子
                    if self.dfn[o] <= self.low[child] and f != -1 and not self.flag[o]:
                        self.flag[o] = True
                    # 找到桥
                    if self.dfn[o] < self.low[child]:
                        self.bridge.append([o, child])
                else:
                    self.low[o] = min(self.low[o], self.dfn[child])
        # root点 儿子数大于等于2
        if f == -1 and c >= 2 and not self.flag[o]:
            self.flag[o] = True
