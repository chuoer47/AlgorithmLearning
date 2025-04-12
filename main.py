from functools import lru_cache, cache


# 预处理出来所有回文数字
def check(x):
    return str(x) == str(x)[::-1]


vaild = [i for i in range(1, 10) if check(i)]

for i in range(1, int(1e5 + 1)):
    # 处理出来偶数长度的回文数字
    n = int(str(i) + str(i)[::-1])
    if check(n):
        vaild.append(n)
    # 处理出来奇数长度的回文数字
    m = str(i)
    n = int(m[:-1] + m[-1] + m[:-1][::-1])
    if check(n):
        vaild.append(n)

vaild = [x for x in set(vaild) if len(str(x)) <= 10]


class Solution:
    @cache
    def countGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        nums = []
        for x in vaild:
            if len(str(x)) == n and x % k == 0:
                nums.append(x)
        vis = set()
        mx = [0] * 10
        for x in nums:
            x = str(x)
            cnt = []
            for i in range(10):
                p = x.count(str(i))
                cnt.append(p)
                mx[i] = max(mx[i], p)
            vis.add(tuple(cnt))

        @cache
        def dfs(bit, limit, state: tuple):
            ans = 0
            for i in range(10):
                if state[i] > mx[i]:
                    return 0
            if bit == 0:
                if state in vis:
                    return 1
                return 0
            for i in range(limit, 9 + 1):
                o = list(state)
                o[i] += 1
                ans += dfs(bit=bit - 1, limit=0, state=tuple(o))
            return ans

        o = [0] * 10
        ans = dfs(n, 1, tuple(o))
        return ans
