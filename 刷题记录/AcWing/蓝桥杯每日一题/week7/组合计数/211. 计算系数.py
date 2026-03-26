"""
https://www.acwing.com/problem/content/213/
"""
from math import factorial

MOD = 10007

a, b, k, n, m, = map(int, input().strip().split(" "))
r = pow(a, n, MOD)
r = (r * pow(b, m, MOD)) % MOD
r = (factorial(k) // (factorial(n) * factorial(k - n)) * r) % MOD
print(r)
