"""
https://www.acwing.com/problem/content/293/
整体思路：
1.进行状态预处理，保证时间复杂度
2.进行DP
"""

while True:
    n, m = map(int, input().split(" "))
    if n == 0 and m == 0:
        break
    st = [True] * (1 << n)
    # 状态预处理
    for i in range(len(st)):
        st[i] = True  # 假设成立
        cnt = 0
        for j in range(n):
            if (i >> j) & 1:  # 第 j 位为1
                if cnt % 2 == 1:  # cnt是奇数
                    st[i] = False
                    break
            else:
                cnt += 1
        if cnt % 2 == 1:  # 特判
            st[i] = False
    f = [[0] * (1 << n) for _ in range(m + 1)]  # (m+1)保证答案f[m+1][0],f[i][j]表示前i-1列排列完毕，第j种排列状态的组合数
    f[0][0] = 1  # 初始化
    # 状压DP
    for i in range(1, m + 1):
        for j in range(1 << n):
            for k in range(1 << n):
                if j & k == 0 and st[j | k]:  # 满足布满i列
                    f[i][j] += f[i - 1][k]
    # 输出答案
    print(f[-1][0])
