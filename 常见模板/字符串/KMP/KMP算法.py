"""
下面为KMP算法
复杂度为O(n+m)
"""


# 前缀函数的编写,太神奇啦
def prefix_function(s):
    sn = len(s)
    pi = [0] * sn
    for i in range(1, sn):
        j = pi[i - 1]
        while j > 0 and s[j] != s[i]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

# 模式匹配如下：
# t = input("输入你要匹配的字符串模式：")
# s = input("输入你要匹配的字符串：")
s = "aaaaa"
t = "aa"


def KMP(s, t):
    """很取巧的写法"""
    sn, tn = len(s), len(t)
    prefixLst = prefix_function(t + "#" + s)
    for i in prefixLst:
        if i == tn:
            return True
    return False


print(KMP(s, t))

