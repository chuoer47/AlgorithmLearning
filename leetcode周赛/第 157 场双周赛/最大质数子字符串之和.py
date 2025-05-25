from math import isqrt


def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, isqrt(x) + 5):
        if i < x and x % i == 0:
            return False
    return True


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        cnt = set()
        for i in range(n):
            for j in range(i, n):
                now = int(s[i:j + 1])
                if is_prime(now):
                    cnt.add(now)
        cnt = sorted(cnt, reverse=True)

        return sum(cnt[:3])
