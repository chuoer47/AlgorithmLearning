"""
https://www.acwing.com/activity/content/code/add/9700/
"""

t = int(input())
arr = [[int(input()), list(map(int, input()))] for _ in range(0, t)]
res = []
for i in range(0, t):
    n,score = arr[i]
    # 生成前缀和
    score_sum = [0]
    for j in range(1, n + 1):
        score_sum.append(score[j - 1] + score_sum[j - 1])
    div = (n+1) // 2
    result = 0
    # 寻找最优解
    for j in range(div, n+1):
        result = max(result, score_sum[j] - score_sum[j-div])
    print("Case #%d: %d"%(i+1,result))
