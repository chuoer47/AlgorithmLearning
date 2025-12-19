class Solution:
    def minMoves(self, balance: List[int]) -> int:
        # 至多一个负数
        sn = sum(balance)
        if sn < 0:
            return -1
        idx = -1
        for i, v in enumerate(balance):
            if v < 0:
                idx = i
                break
        if idx == -1:
            return 0
        d = 1
        ans = 0
        n = len(balance)
        need = -balance[idx]
        while need > 0:
            l, r = (idx - d) % n, (idx + d) % n
            p = [l] if l == r else [l, r]
            for x in p:
                mn = min(need, balance[x])
                need -= mn
                ans += mn * d
            d += 1
        return ans
