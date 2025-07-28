"""
使用暴力的方式实现了一个简答的模式匹配，直接循环比较，时间复杂度为O(mn)
"""

# s = input("输入你要匹配的字符串：")
# t = input("输入你要匹配的字符串模式：")

s = "goodgoogle"
t = "google"
print(s, t)


def findSubString(s, t):
    sn = len(s)
    tn = len(t)
    if sn < tn:
        return False
    sp, tp, np = 0, 0, 0  # 分别为s的下标，t的下标和最新尝试的下标
    while sp < sn or tp < tn:
        if s[sp] == t[tp]:
            sp += 1
            tp += 1
        else:
            np += 1
            sp = np
            tp = 0
    if tp >= tn:
        return True
    else:
        return False


print(findSubString(s, t))
