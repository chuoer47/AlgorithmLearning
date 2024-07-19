"""
https://www.acwing.com/problem/content/534/

相当于找到有这几个货币构成的线性空间的极大无关组的最小数量
"""
def solve(lst):
    max_num = max(lst)
    dp = [0]*(max_num+10)
    dp[0] = 1
    for p in lst:
        for i in range(p,max_num+1):
            dp[i] += dp[i-p]
    res = 0
    for p in lst:
        if lst[p] ==1:
            res+=1
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    weight = list(map(int,input().strip().split(" ")))
    print(solve(weight))