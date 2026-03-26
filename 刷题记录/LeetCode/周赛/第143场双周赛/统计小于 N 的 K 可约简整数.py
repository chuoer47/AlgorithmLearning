# 预处理阶乘以及其逆元
max_n = int(800)
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

N = 800
f = [0]*(N+10)
for i in range(2,N):
    f[i] = f[i.bit_count()] + 1

mod = int(1e9+7)

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        if s == "1":
            return 0
        ans = 0
        n = len(s)
        for g in range(1,n+1): # 枚举1的个数
            if f[g] > k - 1:
                continue
            rem = g
            for i in range(n): # 从大往小遍历...
                if s[i] == "0":
                    continue
                if rem < 0 or n-i-1 <rem:
                    break
                if rem >= 0:
                    ans += myComb(n-1-i,rem)
                    ans%=mod
                rem-=1
        return ans