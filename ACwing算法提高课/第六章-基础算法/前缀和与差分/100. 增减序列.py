"""
https://www.acwing.com/problem/content/description/102/

套模板，直接超时
通过了 0/11个数据
无语啦
"""


def solve(num, lst):
    """计算最少需要多少步将lst变为完成一样的num"""
    n = len(lst)
    tem = [i - num for i in lst] + [0]
    darr = [tem[i] - tem[i - 1] for i in range(n + 1)]  # 差分数组,注意这里是n+1
    t1, t2 = 0, 0
    for i in darr:
        if i > 0:
            t1 += i
        else:
            t2 += -i
    return max(t1, t2)


n = int(input())
lst = [int(input()) for _ in range(n)]
nums = set(lst)
cnt = 0
ans = 2147483649
for num in nums:
    t = solve(num, lst)
    if t < ans:
        ans = t
        cnt = 1
    elif t == ans:
        cnt += 1
# 输出答案
print(ans)
print(cnt)
