# 版本一
class Fenwick:
    __slots__ = 'mx_length', 'mx_cnt'

    def __init__(self, n: int):
        self.mx_length = [0] * (n + 1)
        self.mx_cnt = [0] * (n + 1)

    def lowbit(self, i):
        return i & -i

    def add(self, i: int, length: int, cnt: int):
        while i < len(self.mx_length):
            if self.mx_length[i] == length:
                self.mx_cnt[i] += cnt
            elif self.mx_length[i] < length:
                self.mx_cnt[i] = cnt
                self.mx_length[i] = length
            i += self.lowbit(i)

    def sum(self, i: int):
        length = cnt = 0
        while i > 0:
            if length == self.mx_length[i]:
                cnt += self.mx_cnt[i]
            elif length < self.mx_length[i]:
                cnt = self.mx_cnt[i]
                length = self.mx_length[i]
            i -= self.lowbit(i)
        return length, cnt

# 版本二
class BIT:
    def __init__(self, n):
        self.len = [0] * n
        self.cnt = [0] * n
        self.n = n

    def query(self, i):
        l, c = 0, 0
        while i > 0:
            if self.len[i] > l:
                l = self.len[i]
                c = self.cnt[i]
            elif self.len[i] == l:
                c += self.cnt[i]
            i -= i & -i
        return l, c

    def update(self, i, l, c):
        while i < self.n:
            if self.len[i] < l:
                self.len[i] = l
                self.cnt[i] = c
            elif self.len[i] == l:
                self.cnt[i] += c
            i += i & -i