from functools import cache

# 加速

# 打表
t = 4
MX = 50
S = [{1}]
for i in range(1, t + 1):
    prev = S[i - 1]
    cur = set()
    for x in range(2, MX):
        cnt = bin(x).count('1')
        if cnt in prev:
            cur.add(x)
    S.append(cur)


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1 if n >= 1 else 0

        mx = len(bin(n)[2:])
        A = {x for x in S[k - 1] if x <= mx}
        if not A:
            return 0

        s = bin(n)[2:]
        m = len(s)
        max_A = max(A) if A else 0

        @cache
        def dfs(i, cnt, is_limit):
            # 数位DP模板：
            # i为位置；cnt为1的数量；is_limit表示前面是否一致
            if i == m:
                return int(cnt in A)
            up = int(s[i]) if is_limit else 1
            ans = 0
            for d in range(0, up + 1):
                if cnt + d > max_A:
                    # 剪枝
                    continue
                ans += dfs(i + 1, cnt + d, is_limit and (d == up))
            return ans

        ans = dfs(0, 0, True) - int(1 in A)
        dfs.cache_clear()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.popcountDepth(1, 1))
