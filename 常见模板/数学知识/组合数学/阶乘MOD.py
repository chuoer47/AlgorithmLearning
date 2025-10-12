"""
预处理在质数mod下的阶乘以及阶乘的模逆运算
"""
mod = int(1e9 + 7)
M = 31
fac = [1] * M
for i in range(1, M):
    fac[i] = fac[i - 1] * i % mod
inv_f = [1] * M
inv_f[-1] = pow(fac[-1], -1, mod)
for i in range(M - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % mod
