"""
https://www.acwing.com/problem/content/description/198/
"""


def prime():
    """筛质数的函数"""
    for i in range(2, N):
        if lst[i] == 0:
            table.append(i)
            tem = i
            while tem < N:
                lst[tem] = 1
                tem += i


# 第一步，把1-(2^(31)-1)^0.5 的质数先找到
N = 50010
lst = [0] * N
table = []
prime()

# 第二步，筛[L,R]的质数出来
while True:
    try:
        l, r = map(int, input().strip().split(" "))
    except:
        break

    if l == 1:  # 针对1，特判一下
        l += 1

    if l >= r:  # 特判，虽然题目不会出现这种情况
        print("There are no adjacent primes.")
        continue

    st = [0] * (r - l + 1)  # 作为线性筛选的标记列表
    for i in table:
        if i >= r:
            break
        # 获取大于l而且不等于i的第一个开始元素
        begin = i * (l // i)
        while begin <= i or begin < l:
            begin += i
        # 线性筛选
        while begin <= r:
            st[begin - l] = 1
            begin += i
    primes = [i + l for i in range(r - l + 1) if not st[i]] # 获得质数

    if len(primes) <= 1:
        print("There are no adjacent primes.")
        continue

    # 第三步，完成最大&最小的质数对
    minN, maxN = (r - l + 10), 0
    minPair, maxPair = [], []
    pn = len(primes)
    for i in range(1, pn):
        dis = primes[i] - primes[i - 1]
        if dis < minN:
            minN = dis
            minPair = [primes[i - 1], primes[i]]
        if dis > maxN:
            maxN = dis
            maxPair = [primes[i - 1], primes[i]]
    print("{},{} are closest, {},{} are most distant.".format(minPair[0], minPair[1], maxPair[0], maxPair[1]))
