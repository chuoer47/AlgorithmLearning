"""
https://www.acwing.com/problem/content/description/99/
"""


# 质因数分解模板,p为质因数，g为指数
def factor(n: int, p: list, g: list):
    pivot = -1
    for i in range(2, int(n ** 0.5 + 2)):
        if n % i == 0:
            pivot += 1
        while n % i == 0:
            p[pivot] = i
            g[pivot] += 1
            n = n // i
    if n > 1:
        pivot += 1
        p[pivot] = n
        g[pivot] += 1


mod = 9901
ni = lambda x: pow(x, mod - 2, mod)

if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    if n == 0:
        print(0)
        exit(0)
    f, g = [0] * int(n ** 0.5 + 2), [0] * int(n ** 0.5 + 2)
    factor(n, f, g)
    ans = 1
    for p, k in zip(f, g):
        if not p:
            break
        k = k * m
        if (p - 1) % mod == 0:
            ans = (ans * (k + 1) % mod) % mod
        else:
            ans = (ans * (pow(p, k + 1, mod) - 1) % mod * ni(p - 1) % mod) % mod
    print(ans)
