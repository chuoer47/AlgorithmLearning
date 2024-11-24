def prime_factors(n):
    factor = []
    power = []

    # 处理2的幂次
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factor.append(2)
        power.append(count)

    # 处理奇数因子
    for i in range(3, int(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factor.append(i)
            power.append(count)

    # 如果n是质数且大于2
    if n > 2:
        factor.append(n)
        power.append(1)

    return factor, power

if __name__ == '__main__':
    # 示例
    number = int(input("请输入一个数字: "))
    factors, powers = prime_factors(number)
    print("质因数数组:", factors)
    print("幂次数组:", powers)