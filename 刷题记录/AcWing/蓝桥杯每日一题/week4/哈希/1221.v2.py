"""
https://www.acwing.com/problem/content/1223/
哈希解法
"""
from math import sqrt

n = int(input())
lst_c = [-1]*(2*n+10)
lst_d = [-1]*(2*n+10)
sqrt_n = int(sqrt(n))
for c in range(0,sqrt_n+1):
    for d in range(c,sqrt_n+1):
        t = c*c+d*d
        if lst_c[t]==-1:
            lst_c[t]=c
            lst_d[t]=d
for a in range(0,sqrt_n+1):
    for b in range(a,sqrt_n+1):
        t = n-a*a-b*b
        if lst_c[t]!=-1:
            print(a,b,lst_c[t],lst_d[t])
            exit()