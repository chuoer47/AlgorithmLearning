class Tire:

    def __init__(self, N=100000):
        self.N = N
        self.ne = [[0] * 26 for _ in range(self.N)]  # 存的属性为该结点的编号
        self.cnt = 0  # 存最大编号
        self.exist = [0] * self.N  # 存以该节点结尾的字符串是否存在

    def insert(self, s: str):
        p = 0  # p代表指向第i层的哪个位置
        for i in s:
            c = ord(i) - ord("a")
            if not self.ne[p][c]:
                self.cnt += 1
                self.ne[p][c] = self.cnt
            p = self.ne[p][c]
        self.exist[p] = 1

    def query(self, s):
        """查询是否存在字符串"""
        p = 0
        for i in s:
            c = ord(i) - ord("a")
            if not self.ne[p][c]:
                return False
            p = self.ne[p][c]
        return self.exist[p] == 1
