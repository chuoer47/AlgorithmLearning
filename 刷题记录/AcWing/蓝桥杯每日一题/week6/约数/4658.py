"""
https://www.acwing.com/problem/content/4661/
"""


def solve(n):
    if n == 1:
        return (1,)
    res = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return res


def isPrime(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
s = solve(n)
res = 0
for i in s:
    if isPrime(i):
        res += 1
print(res)
