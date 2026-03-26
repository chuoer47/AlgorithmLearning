class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        s = list(map(lambda x: ord(x) - ord("a"), s))
        cnt = Counter(s)
        # 特判：如果存在eq个单独的字母（区间） 看看能不能直接满足条件
        eq = sum(1 if v == 1 else 0 for k, v in cnt.items())
        if eq >= k:
            return True

        # 遍历最早和最晚出现的位置
        n = len(s)
        maxn = [-1] * 26
        minn = [n] * 26
        for i, v in enumerate(s):
            maxn[v] = max(maxn[v], i)
            minn[v] = min(minn[v], i)

        print(minn,maxn)
        # 找到不为整个字符串的区间 在遍历区间的时候要拓展
        # O(26*n)
        q = []
        for i in range(26):
            if maxn[i] == -1 or minn[i] == n:
                continue
            begin, end = minn[i], maxn[i]
            j = begin
            while j <= end:
                if begin > minn[s[j]]:
                    # 如果到前面 那会访问过，不用再遍历了
                    begin = 0
                    end = n-1
                    break
                end = max(end, maxn[s[j]])
                j += 1

            if begin == 0 and end == n - 1:
                continue
            q.append([begin, end])

        # 找到互不重叠的区间 最多能找到几个
        q.sort()
        tmp = [i for i, j in q]
        m = len(q)
        if m < k:
            return False

        # O(26*log26)
        for i in range(m):
            now = 1
            begin, end = q[i]
            while True:
                idx = bisect_right(tmp, end)
                if idx == m:
                    break
                end = q[idx][1]
                now += 1
            if now >= k:
                return True

        return False