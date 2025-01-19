"""
https://www.acwing.com/problem/content/description/1312/
"""

import math


def C(n, m):  # 从n个里面选m个
    return n * (n - 1) * (n - 2) // 6


m, n = map(int, input().strip().split(" "))
ans = C((m + 1) * (n + 1), 3) - (n + 1) * C(m + 1, 3) - (m + 1) * C(n + 1, 3)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # tem = 0
        # for k in range(1,i):
        #     if k*j%i==0:
        #         tem+=1
        # ans -= 第 433 场周赛*(n-i+1)*(m-j+1)*tem
        ans -= 2 * (n - i + 1) * (m - j + 1) * (math.gcd(i, j) - 1)

print(ans)