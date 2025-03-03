class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            ns = ""
            for i in range(len(s) - 1):
                ns += str((int(s[i]) + int(s[i + 1])) % 10)
            s = ns
            print(s)
        return s[0] == s[1]


s = Solution()
print(s.hasSameDigits("321881"))
# print(s.hasSameDigits("5156184151781515"))
