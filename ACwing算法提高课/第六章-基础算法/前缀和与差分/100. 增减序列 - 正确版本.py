"""
https://www.acwing.com/problem/content/description/102/

AC了，不过函数写得可读性有点差
我只能说好有趣的问题，不过想不出来思路完全不会写呢....
hhh
"""


def solve(num, lst):
    n = len(lst)
    tem = [i - num for i in lst] + [0]
    darr = [tem[i] - tem[i - 1] for i in range(n)]  # 差分数组 注意，这里是n
    t1, t2 = 0, 0
    for i in darr:
        if i > 0:
            t1 += i
        else:
            t2 += -i
    return (t1, t2)  # 返回差分数组中>0的大小，<0的大小


n = int(input())
lst = [int(input()) for _ in range(n)]
pos, neg = solve(lst[0], lst)
# 输出答案
# print(min(pos, neg) + abs(pos - neg))
print(max(pos, neg))
print(abs(pos - neg) + 1)
