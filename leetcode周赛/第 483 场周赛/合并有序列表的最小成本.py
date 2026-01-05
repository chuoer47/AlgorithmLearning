class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        # dfs(state) 合并到state的最小成本
        n = len(lists)
        _len = [len(row) for row in lists]

        @cache
        def get(s):
            if s == 0:
                return 0, 0
            sl = []
            for i in range(n):
                if s >> i & 1:
                    sl.extend(lists[i])
            sl.sort()
            return len(sl), sl[(len(sl) - 1) // 2]

        @cache
        def dfs(state):
            bit_cnt = state.bit_count()
            if bit_cnt == 1:
                return 0
            ans = inf
            sub = (state - 1) & state
            while sub:
                lena, ma = get(sub)
                lenb, mb = get(state ^ sub)
                cost = lena + lenb + abs(ma - mb)
                ans = min(ans, cost + dfs(sub) + dfs(state ^ sub))
                sub = (sub - 1) & state
            return ans

        return dfs((1 << n) - 1)
