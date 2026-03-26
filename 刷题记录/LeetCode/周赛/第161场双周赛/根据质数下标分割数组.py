from typing import List


def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数

    # 从 2 开始遍历到 sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # 将 i 的倍数标记为非质数（从 i*i 开始优化）
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 收集所有标记为质数的数
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


primes = set(sieve_of_eratosthenes(int(1e5 + 100)))


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i, x in enumerate(nums):
            if i in primes:
                a += x
            else:
                b += x
        return abs(a - b)
