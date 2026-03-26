class Solution:
    def processStr(self, s: str, k: int) -> str:
        # 先计算长度 + 特判
        pi = []
        size = 0
        for val in s:
            if val == "*":
                if size > 0:
                    size -= 1
            elif val == "#":
                size *= 2
            elif val == "%":
                pass
            else:
                size += 1
            pi.append(size)
        if k >= size:
            return '.'

        # 反向获取
        # dfs(i,k) 遍历s的前i个操作得到的字符串的 下标为k的字符
        n = len(s)

        def dfs(idx, k):
            val = s[idx]
            length = pi[idx]

            if val == "*":
                return dfs(idx - 1, k)
            elif val == '#':
                if k >= length // 2:
                    return dfs(idx - 1, k - length // 2)
                return dfs(idx - 1, k)
            elif val == '%':
                return dfs(idx - 1, length - k - 1)
            else:
                if k + 1 == length:
                    return val
                return dfs(idx - 1, k)

        ans = dfs(n - 1, k)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.processStr(s="cd%#*#", k=3))
