"""
https://www.acwing.com/problem/content/6/

用朴素的二维dp解决该方法

通过了 12/16个数据 TLE
"""

if __name__ == '__main__':
    n, v = map(int, input().strip().split(" "))
    lst = [0] + [list(map(int, input().strip().split(" "))) for _ in range(n)]
    dp = [[0] * (v + 10) for _ in range(n + 10)]
    for i in range(1, n + 1):
        vi, wi, si = lst[i]
        for j in range(1, v + 1):
            k = 0
            while j - k * vi >= 0 and k <= si:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * vi] + k * wi)
                k += 1
    print(dp[n][v])
