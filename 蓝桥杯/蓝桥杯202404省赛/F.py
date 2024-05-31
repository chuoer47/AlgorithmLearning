"""
小蓝和小乔正在森林里砍柴，它们有 T 根长度分别为 n1, n2, · · · , nT 的木
头。对于每个初始长度为 n 的木头，小蓝和小乔准备进行交替砍柴，小蓝先出
手。每次砍柴时，若当前木头长度为 x ，需要砍下一截长度为 p 的木头，然后
换另一个人继续砍，其中 2 ≤ p ≤ x 且 p 必须为质数。当轮到某一方时 x = 1 或
x = 0 ，它就没法继续砍柴，它就输了。它们会使用最优策略进行砍柴。请对每
根木头判断是小蓝赢还是小乔赢，如果小蓝赢请输出 1 （数字 1），如果小乔赢
请输出 0 （数字 0）。
"""
import math


def is_prime(x):
    if x <= 3:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solve(x, turn):  # 小兰的回合则为False,不是为True
    if x == 0 or x == 1:
        return turn  # 是小兰的回合则为输了,反之则赢了
    if x != 0 and x != 1 and is_prime(x):
        return not turn  # 是小兰的回合则为赢了，反之则输了
    # 下面进行暴搜
    flag = False
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            # print("turn={}".format(turn))
            # print("i={}".format(i))
            flag = solve(x - i, not turn)
            if flag:  # 有赢的机会
                return True  # 终止
    return False  # 尝试所有机会，没有赢的可能


n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

res = []
for i in range(n):
    t = solve(lst[i], False)  # 0表示小蓝回合，1表示小乔回合
    if t:
        res.append(1)
    else:
        res.append(0)
for i in range(n):
    print(res[i])
