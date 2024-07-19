"""
https://www.acwing.com/problem/content/description/1022/
"""

m,n = map(int,input().strip().split(" "))
k = int(input())
lst = [list(map(int,input().strip().split(" "))) for _ in range(k)]
dp = [[9999999]*(n+10) for _ in range(m+10)]
dp[0][0] = 0
for a,b,c in lst:
    for i in range(m,-1,-1):
        for j in range(n,-1,-1):
            dp[i][j] = min(dp[i][j],dp[max(0,i-a)][max(0,j-b)]+c)
print(dp[m][n])