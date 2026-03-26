"""
https://www.acwing.com/problem/content/425/
"""

if __name__ == '__main__':
    t, m = map(int, input().split(" "))
    lst = [list(map(int, input().split(" "))) for _ in range(m)]
    # lst.sort()
    dp = [0] * (t + 10)
    for w, v in lst:
        for i in range(t, w-1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    print(dp[t])
