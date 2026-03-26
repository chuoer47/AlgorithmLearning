"""
https://www.luogu.com.cn/problem/P1618
利用全排序
"""
import itertools


def check(aa, bb, cc):
    k1 = aa / a
    k2 = bb / b
    k3 = cc / c
    return k1 == k2 and k2 == k3


def cal(l, r):
    res = 0
    for i in range(l + 1, r + 1):
        res = sub_lst[i] + res * 10
    return res


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    if 0 in (a, b, c): # 特例判断
        print("No!!!")
    else:
        lst = [i for i in range(1, 10)]
        arr = itertools.permutations(lst)  # 利用全排序
        res = []
        sub_lst = []
        for sub_lst in arr:
            for i in range(0, 6):  # 可以思考为什么取6
                for j in range(i + 1, 9):
                    aa = cal(-1, i)
                    bb = cal(i, j)
                    cc = cal(j, 8)
                    if check(aa, bb, cc):
                        res.append((aa, bb, cc))
        if not res:
            print("No!!!")
        else:
            res.sort()
            for aa, bb, cc in res:
                print(aa, bb, cc)
