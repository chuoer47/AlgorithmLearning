"""
前缀函数&KMP
"""


def prefix_function(s):
    n = len(s)
    pi = [0]
    for i in range(1, n):
        p = pi[-1]
        while p > 0 and s[i] != s[p]:
            p = pi[p - 1]
        if s[i] == s[p]:
            p += 1
        pi.append(p)
    return pi


def KMP(s, p):
    """s为字符串，p为待匹配的模式"""
    pi = prefix_function(p + "#" + s)
    l1, l2 = len(s), len(p)
    for i in range(l2, l1 + l2 + 1):
        if pi[i] == l2:
            return True
    return False


if __name__ == '__main__':
    print(KMP("abaa", "aba"))
