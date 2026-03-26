"""
https://www.acwing.com/problem/content/199/
"""

from collections import Counter

n = int(input())
prime_lst = [True] * (n + 10)
prime = []
ct = Counter()
# 素数筛
for i in range(2, n + 1):
    if prime_lst[i]:
        prime.append(i)
        j = 2 * i
        while j <= n:
            prime_lst[j] = False
            j += i

# 贡献法：简直巧妙
for p in prime:
    pp = p
    while pp <= n:
        ct[p] += n // pp
        pp *= p
for i in ct:
    print("{} {}".format(i, ct[i]))
