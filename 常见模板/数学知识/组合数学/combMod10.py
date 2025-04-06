def comb_mod10(n: int, m: int) -> int:
    if m < 0 or m > n:
        return 0
    if m == 0:
        return 1

    def mod2(n: int, m: int) -> int:
        return 1 if (n & m) == m else 0

    # 使用Lucas定理
    def mod5(n: int, m: int) -> int:
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
