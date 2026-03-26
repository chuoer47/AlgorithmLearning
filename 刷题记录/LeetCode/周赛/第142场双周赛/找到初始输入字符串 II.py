from itertools import accumulate


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = int(1e9 + 7)
        n = len(word)
        exp = []  # 计算指数

        # 先计算有效方案
        now = word[0]
        cnt = 0
        for c in word + "#":
            if c == now:
                cnt += 1
            else:
                now = c
                exp.append(cnt)
                cnt = 1
        vaild = 1  # 计算有效的方案数目
        for i in exp:
            vaild = (vaild * i) % mod

        m = len(exp)
        if m >= k:  # 神仙剪枝
            return vaild
        # 使用DP计算无效方案

        # 利用前缀和快速计算状态转移
        dp = [[0] * (k + 10) for _ in range(m + 10)]
        dp[0][0] = 1
        pre = list(accumulate(dp[0], initial=0))
        for i in range(1, m + 1):
            for j in range(k):
                t = min(j, exp[i - 1])
                dp[i][j] += pre[j] - pre[j - t]
            pre = list(accumulate(dp[i], initial=0))

        nonvaild = (sum(dp[m])) % mod
        return (vaild - nonvaild) % mod


if __name__ == '__main__':
    s = Solution()
    print(s.possibleStringCount(word="aaabbb", k=3))
