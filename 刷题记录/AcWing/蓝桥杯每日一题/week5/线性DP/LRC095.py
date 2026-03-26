"""
https://leetcode.cn/problems/qJnOS7/
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0] * n2 for _ in range(n1)]
    # 初始化第一行和第一列,写的稍微复杂了点
    flag = 0
    for i in range(n1):
        j = 0
        if text1[i] == text2[j]:
            flag = 1
        dp[i][j] = flag
    flag = 0
    for j in range(n2):
        i = 0
        if text1[i] == text2[j]:
            flag = 1
        dp[i][j] = flag
    for i in range(1, n1):
        for j in range(1, n2):
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
res = longestCommonSubsequence(text1=text1, text2=text2)
print(res)
