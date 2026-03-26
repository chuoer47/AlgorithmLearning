"""
通过率 99.1 %
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # write code here
        i, j = 0, 0
        ns, np = len(s), len(p)
        while i < ns and j < np:
            # 分类讨论
            if p[j] == "*":
                while j < np - 1 and p[j + 1] == "*":
                    j += 1
                if j + 1 >= np:
                    return True
                elif (p[j + 1] == s[i] or p[j + 1] == '?' or p[j + 1] == "*") and self.isMatch(s[i:], p[j + 1:]):
                    return True
                else:
                    i += 1
            elif (s[i] == p[j] or p[j] == '?') and p[j] != "*":  # 可直接匹配的情况
                i += 1
                j += 1
            else:
                return False
        while j < np and p[j] == "*":
            j += 1
        return i == ns and j == np


if __name__ == '__main__':
    S = Solution()
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    print(S.isMatch(s, p))
