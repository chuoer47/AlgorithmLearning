def euler_sieve(n: int) -> list:
    """使用欧拉筛（Euler's Sieve）筛选出小于等于n的所有质数

    算法特点：
    - 时间复杂度：O(n)，每个合数仅被其最小质因数标记一次
    - 空间复杂度：O(n)，需要两个数组存储标记和质数列表
    - 适用场景：需要高效筛选较大范围内质数的场景（如数论问题、素性判断等）

    参数:
        n: 筛选质数的上限（包含n本身）

    返回:
        list: 所有小于等于n的质数组成的列表，按升序排列

    示例:
        >>> euler_sieve(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if n < 2:
        return []  # 小于2的数没有质数

    # is_prime[i]为True表示i是质数，初始全部假设为质数（True）
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数

    primes = []  # 存储筛选出的质数

    for i in range(2, n + 1):
        # 若当前数未被标记为合数，则它是质数
        if is_prime[i]:
            primes.append(i)

        # 用当前质数列表中的质数标记合数
        # 遍历条件：质数列表不为空，且当前质数与i的乘积不超过n
        for p in primes:
            if p * i > n:
                break  # 超出范围，停止标记

            # 标记i*p为合数（非质数）
            is_prime[p * i] = False

            # 关键优化：当i能被p整除时，p是i的最小质因数，停止循环
            # 确保每个合数只被其最小质因数标记一次
            if i % p == 0:
                break

    return primes


n = 100
primes = set(euler_sieve(n))

# 使用示例
if __name__ == "__main__":
    # 筛选100以内的所有质数
    max_num = 100
    prime_list = euler_sieve(max_num)
    print(f"小于等于{max_num}的质数有：")
    print(prime_list)
    print(f"共{len(prime_list)}个")
