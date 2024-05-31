"""
纯纯无聊，试试看能用最少几行写完
"""


def fun(n: int, res, MOD) -> int:
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            res = res * (i - 1) // i
            while n % i == 0:
                n //= i
    return res if n == 1 else res * (n - 1) // n


a, b = map(int, input().split())
print(0 if a == 1 else pow(a, b - 1, 998244353) * fun(a, a, 998244353) % 998244353)
