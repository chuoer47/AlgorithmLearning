s = "bba"
t = "ba"


class Solution:
    def check(self, cnt_s, cnt_t):
        for item in cnt_t.keys():
            if cnt_s[item] < cnt_t[item]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        cnt_t = Counter(t)
        cnt_s = Counter(s)
        if not self.check(cnt_s, cnt_t):
            return ""
        t_set = set(t)
        l, r = 0, 0
        cnt_s = Counter()
        ans = s
        flag = False  # 减少时间开销
        while r < len(s) or flag:
            while r < len(s) and not flag:
                cnt_s[s[r]] += 1
                r += 1
                flag = self.check(cnt_s, cnt_t)
            while l < len(s) and s[l] not in t_set:
                l += 1
            if flag and r - l < len(ans):
                ans = s[l:r]
            if l < len(s):
                cnt_s[s[l]] -= 1
                flag = self.check(cnt_s, cnt_t)
                l += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(s, t))
