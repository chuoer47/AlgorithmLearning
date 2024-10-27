class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        word += "#"
        now = "#"
        cnt = 1
        for c in word:
            if c == now:
                cnt += 1
            else:
                now = c
                ans += cnt - 1
                cnt = 1
        return ans
