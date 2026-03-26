from collections import defaultdict
from typing import List

# 预处理阶乘以及其逆元
max_n = int(1e6)
fac = [1] * (max_n + 1)
facinv = [1] * (max_n + 1)

MAX_NUM = int(1e9 + 7)
for i in range(1, max_n + 1):
    fac[i] = fac[i - 1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i], MAX_NUM - 2, MAX_NUM)


def myComb(n, m):
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n - m] % MAX_NUM


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        mapper = defaultdict(int)
        for x, y in points:
            mapper[y] += 1
        value = list(mapper.values())
        num = []
        ans = 0
        for v in value:
            if v >= 2:
                num.append(myComb(v, 2))
            else:
                num.append(0)
        pre = 0
        for v in num:
            ans = (ans + v * pre) % mod
            pre = (pre + v) % mod
        return ans
