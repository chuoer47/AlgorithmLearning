class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel = "aeiou"
        p = "qwertyuiopasdfghjklzxcvbnm"
        cnt1 = cnt2 = 0
        for x in s:
            cnt1 += int(x in vowel)
            cnt2 += int(x not in vowel and x in p)
        return 0 if cnt2 == 0 else cnt1 // cnt2