def solve(num, lst):
    """计算最少需要多少步将lst变为完成一样的num"""
    n = len(lst)
    tem = [i - num for i in lst] + [0]
    darr = [tem[i] - tem[i - 1] for i in range(n+1)]  # 差分数组
    t1, t2 = 0, 0
    for i in darr:
        if i > 0:
            t1 += i
        else:
            t2 += -i
    return max(t1, t2)

n = int(input())
t1 = list(map(int,input().strip().split(" ")))
t2 = list(map(int,input().strip().split(" ")))
lst = [t1[i]-t2[i] for i in range(n)]
print(solve(0,lst))