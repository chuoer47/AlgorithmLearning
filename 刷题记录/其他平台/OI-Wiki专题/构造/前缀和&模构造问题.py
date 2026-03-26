"""
https://www.luogu.com.cn/problem/P3599

Task1：试判断能否构造并构造一个长度为 n 的 1... n 的排列，满足其 n 个前缀和在模 n 的意义下互不相同

Task2：试判断能否构造并构造一个长度为 n 的 1... n 的排列，满足其 n 个前缀积在模 n 的意义下互不相同

Task1:
当 n 为奇数时，无法构造出合法解；

当 n 为偶数时，可以构造一个形如 n,1,n-2,3,... 这样的数列。

首先，我们可以发现 n 必定出现在数列的第一位，否则 n 出现前后的两个前缀和必然会陷入模意义下相等的尴尬境地；

然后，我们考虑构造出整个序列的方式：

考虑通过构造前缀和序列的方式来获得原数列，可以发现前缀和序列两两之间的差在模意义下不能相等，因为前缀和序列的差分序列对应着原来的排列。

Task2:
当 n 为除 4 以外的合数时，无法构造出合法解

当 n 为质数或 4 时，可以构造一个形如

\dfrac{2}{1},\dfrac{3}{2},\cdots,\dfrac{n-1}{n-2},n 这样的数列

先考虑什么时候有解：

显然，当 n 为合数时无解。因为对于一个合数来说，存在两个比它小的数 p,q
我们考虑如何构造这个数列：

和 task1 同样的思路，我们发现 1 必定出现在数列的第一位，否则 1 出现前后的两个前缀积必然相等；
而 n 必定出现在数列的最后一位，因为 n 出现位置后的所有前缀积在模意义下都为 0。
分析题目给出的几组样例以后发现，所有样例中均有一组合法解满足前缀积在模意义下为 1,2,3,...,n
因此我们可以构造出上文所述的数列来满足这个条件。那么我们只需证明这 n 个数互不相同即可。
"""


def task1(n):
    if n == 1:
        return [2, 1]
    if n % 2 and n != 1:
        return [0]
    res = [2]
    sgn = 1
    sgn2 = -1
    for i in range(n):
        res.append(sgn * n + sgn2 * i)
        sgn = (sgn - 1) * (-1)
        sgn2 *= -1
    return res


def isPrime(n):
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def task2(n):
    if n == 1:
        return [2, 1]
    elif n == 4:
        return [2, 1, 3, 2, 4]
    elif not isPrime(n):
        return [0]
    else:
        res = [2, 1]
        for i in range(2, n):
            res.append((i * pow(i - 1, n - 2, n)) % n)
        res.append(n)
        return res


x, t = map(int, input().strip().split(" "))
if x == 1:
    task = task1
else:
    task = task2
for _ in range(t):
    n = int(input())
    print(*task(n))

# print(isPrime(3))
