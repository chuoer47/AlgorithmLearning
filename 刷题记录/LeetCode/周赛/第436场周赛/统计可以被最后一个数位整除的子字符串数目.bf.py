class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            c = s[i]
            if c == "0":
                continue
            elif c in "125":
                ans += i + 1
                print(ans)
                continue
            c = int(c)
            base = 1
            now = 0
            j = i
            while j >= 0:
                nc = int(s[j])
                now = (now + nc * base) % c
                base = (base * 10) % c
                if now % c == 0:
                    ans += 1
                j -= 1
            print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings(s="5701283"))
