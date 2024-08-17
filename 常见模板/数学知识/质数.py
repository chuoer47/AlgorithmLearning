"""下面为筛选质数的代码"""
N = 1000010
lst = [0] * N
table = []


def prime():
    """筛质数的函数"""
    for i in range(2, N):
        if lst[i] == 0:
            table.append(i)
            tem = i
            while tem < N:
                lst[tem] = 1
                tem += i
