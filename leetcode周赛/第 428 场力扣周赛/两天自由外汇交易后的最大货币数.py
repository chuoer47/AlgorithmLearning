class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                  rates2: List[float]) -> float:
        ans = 1
        n, m = len(pairs1), len(pairs2)

        def trans(pairs, rate):
            ans = Counter()
            g = defaultdict(list)
            for i, (u, v) in enumerate(pairs):
                g[u].append((v, rate[i]))
                g[v].append((u, 1 / rate[i]))

            def dfs(now, fa, v):
                for nxt, r in g[now]:
                    if nxt == fa:
                        continue
                    ans[nxt] = max(ans[nxt], v * r)
                    dfs(nxt, now, v * r)

            dfs(initialCurrency, "#", 1)
            return ans

        day1 = trans(pairs1, rates1)
        # print(day1)
        day2 = trans(pairs2, rates2)
        # print(day2)
        ans = 1
        for k, v in day1.items():
            if day2[k] == 0:
                continue
            ans = max(ans, v / day2[k])
        return ans
