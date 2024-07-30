"""
https://www.acwing.com/problem/content/1066/
dp[i][j][k] 前i行摆好，有j个棋子已经就位，状态为k

该方法没有优化，TLE
需要提前处理数组
"""


def binLen(s):
    return bin(s).count("1")


def noGood(n):
    s = "#" + bin(n)[2:] + "#"
    for i in range(1, len(s) - 1):
        if s[i] == "1":
            if s[i - 1] == "1" or s[i + 1] == "1":
                return True
    return False


def check(t, k):
    if binLen(k) + binLen(t) > K:
        return False
    if noGood(k) or noGood(t):
        return False
    if ((t << 1) & k) or ((k << 1) & t) or (t & k):
        return False
    return True


n, K = map(int, input().split())
N = 11
dp = [[[0] * (1 << n) for _ in range(K + 1)] for _ in range(N)]
dp[0][0][0] = 1
for i in range(1, n + 1):
    for j in range(0, K + 1):
        for k in range(1 << n):
            for t in range(1 << n):
                if check(k, t):
                    if j - binLen(k) >= 0:
                        dp[i][j][k] += dp[i - 1][j - binLen(k)][t]
print(sum(dp[n][K]))
