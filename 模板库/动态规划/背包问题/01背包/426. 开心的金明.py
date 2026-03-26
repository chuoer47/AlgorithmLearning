"""
https://www.acwing.com/problem/content/description/428/

dp[i][j] i:购买物品个数 j:钱数 属性：最大价值

dp[i][j] = max{ dp[i][j], dp[i-1][j-p]+w }  p,w为枚举量
"""

n, m = map(int, input().strip().split(" "))
lst = [list(map(int, input().split(" "))) for _ in range(m)]
for i in lst:
    i[1] *= i[0]
dp = [[0]*(n+10) for _ in range(m+10)]
for p,w in lst: # 枚举商品
    for i in range(m,0,-1):
        for j in range(n,p-1,-1):
            dp[i][j] = max(dp[i][j],dp[i-1][j-p]+w)
print(dp[m][n])