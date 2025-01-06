"""
核心思想如下：
s[0...r] = s[0]*B^r + s[1]*B^(r-1) + ... + s[r]*B^0
s[0...l] = s[0]*B^l + s[1]*B^(l-1) + ... + s[l]*B^0
s[l+1...r] = s[0...r] - s[0...l]*B^(r-l)
"""

# 可改变
MOD = 10 ** 9 + 7
base = 52
MX = 5000
f = [1] * (MX + 1)
for i in range(1, MX + 1):
    f[i] = f[i - 1] * base % MOD


def hash_str(nums):
    # 返回类似前缀和的数组hval
    n = len(nums)
    hval = [0] * (n + 1)
    for i, x in enumerate(nums):
        hval[i + 1] = (hval[i] * base + x) % MOD
    return hval


def substr(l, r, hval):
    # [l,r] 左闭右闭的字符串
    return (hval[r + 1] - hval[l] * f[r + 1 - l]) % MOD
