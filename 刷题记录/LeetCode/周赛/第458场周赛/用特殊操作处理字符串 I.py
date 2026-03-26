class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for val in s:
            if val == '*':
                if ans:
                    ans.pop()
            elif val == '#':
                ans = ans + ans
            elif val == '%':
                ans = ans[::-1]
            else:
                ans.append(val)
        return "".join(ans)
