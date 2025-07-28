# 预处理阶乘以及其逆元（需要根据题目情况自定义修改）
max_n = int(80)
fac = [1] * (max_n + 1)
facinv = [1] * (max_n + 1)

MAX_NUM = int(1e9 + 7)
for i in range(1, max_n + 1):
    fac[i] = fac[i - 1] * i % MAX_NUM
    facinv[i] = pow(fac[i], MAX_NUM - 2, MAX_NUM)  # python自带快速幂


def myComb(n, m):
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n - m] % MAX_NUM
