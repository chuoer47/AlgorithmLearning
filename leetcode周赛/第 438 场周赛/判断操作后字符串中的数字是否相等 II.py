from functools import cache


@cache
def myComb(n, m):
    # 记忆化咯
    return comb_mod10(n, m)


def comb_mod10(n: int, m: int) -> int:
    # 傻逼题目非要mod10 给个质数会死啊
    if m < 0 or m > n:
        return 0
    if m == 0:
        return 1

    def mod2(n: int, m: int) -> int:
        return 1 if (n & m) == m else 0

    # 使用Lucas定理
    def mod5(n: int, m: int) -> int:
        # 抄的
        mod5_table = [
            [1, 0, 0, 0, 0],  # a=0
            [1, 1, 0, 0, 0],  # a=1
            [1, 2, 1, 0, 0],  # a=2
            [1, 3, 3, 1, 0],  # a=3
            [1, 4, 1, 4, 1],  # a=4
        ]
        result = 1
        while n > 0 or m > 0:
            ni = n % 5  # 当前五进制位
            mi = m % 5
            if mi > ni:  # 若某一位 m > n，结果为0
                return 0
            result = (result * mod5_table[ni][mi]) % 5
            n //= 5
            m //= 5
        return result

    a = mod2(n, m)
    b = mod5(n, m)
    return (5 * ((a - b) % 2) + b) % 10


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        mod = 10
        s = list(map(int, s))
        n = len(s)
        m = n - 1
        x1 = 0
        for i in range(1, n):
            x1 = (x1 + s[i - 1] * myComb(m - 1, i - 1)) % 10
        x2 = 0
        for i in range(1, n):
            x2 = (x2 + s[i] * myComb(m - 1, i - 1)) % 10
        return x1 == x2

if __name__ == '__main__':
    s = Solution()
    print(s.hasSameDigits("5156184151781515"))
